import initialFormData from "./formData";
import Alpine from 'alpinejs';
import persist from '@alpinejs/persist';

export function setupFormData() {
    return {
        formData: initialFormData,
        getTableHeaders: () => {
            let headers: string[] = []
            document.querySelectorAll("table th").forEach(header => {
                if (header && header.textContent) {
                    headers.push(header.textContent)
                }
            })
            return headers

        },
        sectionFilters: Alpine.$persist({
            personal: true,
            debt: true,
            retirement: true,
            income: true,
            taxes: true,
            savings: true,
            deferred: true,
            employer: true,
            ira: true,
            taxable: true,
            targets: true,
            extra: true,

        }),
        columns: Alpine.$persist(RetirementCalculator.table.columns),
        results: [],

        init() {
            this.$watch('formData', () => {
                this.fillTable()
            });
            this.fillTable();
        },
        formatValue: (value, format) => {
            console.log(value, format)
            if (format === 'currency') {
                return value.toLocaleString('en-US', {style: 'currency', currency: 'USD'})
            }

            return value
        },


        RetirementStrategies: {
            age: (row) => row.age === row.retirementAge,
            percent_rule: (row) => row.savingsEndOfYear * row.retirementWithdrawalRate / 100 > row.retirementIncomeGoal,
            target_savings: (row) => row.retirementSavingsAmount >= row.savingsEndOfYear,
            debt_free: (row) => row.debt <= 0
        },


        InflationGrowthStrategies: {
            fixed: (row) => row.inflationRate,
            percentage_increase: (row) => row.inflationRate * (1 + row.inflationRate / 100),
        },

        IncomeTaxStrategies: {
            simple: (row) => row.incomeTaxable * row.incomeTaxRate / 100,
            bracket: (row) => row.incomeTaxable * row.incomeTaxRate / 100,
        },

        initializeTableRow(formData) {
            let curRow = JSON.parse(JSON.stringify(formData));
            /* TODO Need to account for employer contribution more than the employee. Goal is to maximize savings */

            /* Initialization */


            curRow = RetirementCalculator.pipeline.endOfYearPipeline.initialize(curRow)


            return curRow;

        }, updateRow(previousRow) {
            let curRow = JSON.parse(JSON.stringify(previousRow));


            curRow = RetirementCalculator.pipeline.startOfYearPipeline.process(curRow)
            curRow = RetirementCalculator.process.electiveLimit.process(curRow)
            curRow = RetirementCalculator.pipeline.taxDeferredPipeline.process(curRow)
            curRow = RetirementCalculator.pipeline.taxDeferredEmployerMatchPipeline.process(curRow)
            curRow = RetirementCalculator.pipeline.taxableSavingsPipeline.process(curRow)
            curRow = RetirementCalculator.pipeline.iraTaxableSavingsPipeline.process(curRow)
            curRow = RetirementCalculator.pipeline.iraTaxDeferredSavingsPipeline.process(curRow)
            curRow = RetirementCalculator.pipeline.endOfYearPipeline.process(curRow)
            return curRow;
        }, fillTable() {
            let firstRow = this.initializeTableRow(this.formData);
            let table = [firstRow];
            let rowIndex = 0

            while (table[rowIndex].age <= table[rowIndex].lifeExpectancy && !this.RetirementStrategies[this.formData.retirementStrategy](table[rowIndex])) {
                let previousRow = table[rowIndex];
                let curRow = this.updateRow(previousRow);
                table.push(curRow);
                rowIndex += 1;

            }

            this.results = table;
        },
    }
}