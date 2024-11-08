import {Row} from "../interfaces/Row";
import {Pipeline} from "../interfaces/Pipeline";

export default class StartOfYearPipeline implements Pipeline {

    initialize(row: Row): Row {
        row.taxDeferredSpending = 0
        row.taxableSpending = 0
        return row
    }

    process(row: Row): Row {
        row.age += 1
        row.year += 1
        row.retirementIncomeGoal += row.retirementIncomeGoal * row.inflationRate / 100
        row.taxDeferredSpending = 0
        row.taxableSpending = 0
        return row
    }

}