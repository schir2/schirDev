from django import forms
from django.utils import timezone


class RetirementCalculatorForm(forms.Form):
    INFLATION_GROWTH_STRATEGY_CHOICES = [
        ('fixed', 'Fixed'),
        ('percentage_increase', 'Percentage Increase'),
    ]
    EXPENSE_GROWTH_STRATEGY_CHOICES = [
        ('fixed', 'Fixed'),
        ('percent_of_income', 'Percentage of Income'),
    ]

    INCOME_GROWTH_STRATEGY_CHOICES = [
        ('fixed', 'Fixed'),
        ('percentage_increase', 'Percentage Increase'),
    ]

    INCOME_TAX_STRATEGY_CHOICES = [
        ('simple', 'Simple'),
        ('bracket', 'Bracket'),
    ]

    FILING_STATUS_CHOICES = [
        ('single', 'Single'),
        ('married_joint', 'Married Filing Jointly'),
        ('married_separate', 'Married Filing Separately'),
        ('head_household', 'Head of Household'),
    ]

    BANK_CONTRIBUTION_STRATEGY_CHOICES = [
        ('fixed', 'Fixed'),
        ('percent_of_income', 'Percent of Income'),
    ]

    TAX_DEFERRED_CONTRIBUTION_STRATEGY_CHOICES = [
        ('fixed', 'Fixed Contribution'),
        ('percent_of_income', 'Percentage of Income'),
        ('until_company_match', 'Until Employer Match Met'),
        ('max', 'Max Out'),
    ]

    TAXABLE_CONTRIBUTION_STRATEGY_CHOICES = [
        ('fixed', 'Fixed Contribution'),
        ('percent_of_income', 'Percentage of Income'),
    ]

    IRA_CONTRIBUTION_STRATEGY_CHOICES = [
        ('fixed', 'Fixed Contribution'),
        ('percent_of_income', 'Percentage of Income'),
        ('max', 'Max Out')
    ]

    EMPLOYER_CONTRIBUTION_STRATEGY_CHOICES = [
        ('none', 'Does not contribute'),
        ('percentage_of_contribution', 'Match Percentage of Contribution'),
        ('percentage_of_compensation', 'Percentage of Compensation'),
        ('fixed', 'Fixed Amount'),
    ]

    EXPENSES_GROWTH_STRATEGY_CHOICES = [
        ('fixed', 'Fixed'),
        ('percentage_increase', 'Percentage Increase'),
    ]

    WITHDRAWAL_STRATEGY_CHOICES = [
        ('sequential', 'Sequential'),
        ('proportional', 'Proportional'),
        ('tax_bracket_management', 'Tax Bracket Management'),
        ('roth_conversion_ladder', 'Roth Conversion Ladder'),
        ('bridging', 'Bridging'),

    ]

    RETIREMENT_STRATEGY_CHOICES = [
        ('age', 'Retire at a Specific Age'),
        ('percent_rule', 'Retire When the % Rule Is Met'),
        ('target_savings', 'Retire When a Target Savings Amount Is Reached'),
        ('debt_free', 'Retire When Debt Is Eliminated'),
    ]

    CASH_MAINTENANCE_STRATEGY_CHOICES = [
        ('fixed', 'Fixed Cash Maintenance'),
        ('variable_cash_reserve', 'Variable Cash Reserve'),
        ('percentage_of_portfolio', 'Percentage of Portfolio'),
    ]

    age = forms.IntegerField(
        min_value=0,
        max_value=100,
        initial=30,
        label="Age",
        help_text="Your current age in years.",
    )

    retirement_strategy = forms.ChoiceField(
        choices=RETIREMENT_STRATEGY_CHOICES,
        initial='age',
        label='Retirement Strategy',
        help_text='Select the strategy that dictates when you plan to retire and stop investing.',
    )

    retirement_expenses = forms.FloatField(
        min_value=0,
        label='Annual Retirement Expenses',
        help_text='Your expected annual expenses during retirement.',
    )

    retirement_savings_amount = forms.FloatField(
        min_value=0,
        label='Target Savings Amount',
        help_text='The total savings amount you aim to reach before retiring.',
    )

    retirement_withdrawal_rate = forms.FloatField(
        min_value=0,
        initial=4.0,
        label='Retirement Rate of Withdrawal',
        help_text='Enter the percentage of your retirement savings you plan to withdraw annually (e.g., 4 for 4%).'
    )

    year = forms.IntegerField(
        min_value=0,
        max_value=100,
        initial=timezone.now().year,
        label="Year",
        help_text="Starting Year",
    )

    retirement_age = forms.IntegerField(
        min_value=0,
        max_value=100,
        initial=65,
        label="Retirement Age",
        help_text="The age at which you plan to retire.",
    )

    life_expectancy = forms.IntegerField(
        min_value=0,
        max_value=100,
        initial=85,
        label="Life Expectancy",
        help_text="Your estimated life expectancy in years.",
    )

    tax_deferred_savings = forms.IntegerField(
        min_value=0,
        initial=100000,
        label="Tax-Deferred Savings",
        help_text="Your current savings in tax-deferred accounts (e.g., 401(k), Traditional IRA).",
    )

    tax_deferred_growth_rate = forms.FloatField(
        min_value=0,
        initial=6.0,
        label="Tax-Deferred Growth Rate (%)",
        help_text="Expected annual growth rate for tax-deferred savings as a percentage.",
    )

    taxable_savings = forms.IntegerField(
        min_value=0,
        initial=50000,
        label="Taxable Savings",
        help_text="Your current savings in taxable accounts.",
    )

    ira_savings = forms.IntegerField(
        min_value=0,
        initial=30000,
        label="Tax-Exempt Savings",
        help_text="Your current savings in tax-exempt accounts (e.g., Roth IRA).",
    )

    cash = forms.IntegerField(
        min_value=0,
        initial=20000,
        label="Cash",
        help_text="Your current bank savings (e.g., checking, savings accounts).",
    )

    cash_maintenance_strategy = forms.ChoiceField(
        choices=CASH_MAINTENANCE_STRATEGY_CHOICES,
        initial='fixed',
        label="Cash Maintenance Strategy",
        help_text="Strategies for maintaining cash.",
    )

    cash_maintenance_target_amount = forms.IntegerField(
        min_value=0,
        initial=0,
        label="Cash Maintenance Target Amount",
    )

    cash_maintenance_months_of_expenses_in_reserve= forms.IntegerField(
        min_value=0,
        initial=6,
        label="Cash Maintenance Number of Month Expenses",
    )

    annual_taxable_contribution = forms.IntegerField(
        min_value=0,
        initial=500,
        label="Annual Taxable Contribution",
        help_text="Your annual contribution to taxable savings accounts.",
    )

    tax_deferred_contribution_fixed_amount = forms.IntegerField(
        min_value=0,
        initial=1000,
        label="Annual Tax-Deferred Contribution",
        help_text="Your annual contribution to tax-deferred accounts.",
    )

    tax_deferred_contribution_percentage = forms.FloatField(
        min_value=0,
        max_value=100,
        initial=5.0,
        label="Tax-Deferred Contribution Percentage",
        help_text="The percentage of your pre-tax income to contribute to tax-deferred accounts.",
    )

    ira_contribution_percentage = forms.FloatField(
        min_value=0,
        max_value=100,
        initial=5.0,
        label="Tax-Exempt Contribution Percentage",
        help_text="The percentage of your pre-tax income to contribute to tax-exempt accounts (e.g., Roth IRA).",
    )

    taxable_contribution_percentage = forms.FloatField(
        min_value=0,
        max_value=100,
        initial=5.0,
        label="Taxable Contribution Percentage",
        help_text="The percentage of your pre-tax income to contribute to taxable accounts.",
    )

    employer_match_percentage_limit = forms.FloatField(
        min_value=0,
        max_value=100,
        initial=3.0,
        label="Employer Match Percentage Limit (%)",
        help_text="The maximum percentage of your compensation that your employer will match.",
    )

    employer_match_percentage = forms.FloatField(
        min_value=0,
        max_value=100,
        initial=100.0,
        label="Employer Match Percentage (%)",
        help_text="The percentage of your contribution that your employer will match.",
    )

    ira_contribution_fixed_amount = forms.IntegerField(
        min_value=0,
        initial=500,
        label="Annual Tax-Exempt Contribution",
        help_text="Your annual contribution to tax-exempt accounts (e.g., Roth IRA).",
    )

    expenses = forms.IntegerField(
        min_value=0,
        initial=40000,
        label="Annual Expenses",
        help_text="Your estimated annual living expenses.",
    )

    inflation_rate = forms.FloatField(
        min_value=0,
        initial=2.0,
        label="Inflation Rate (%)",
        help_text="Expected annual inflation rate as a percentage.",
    )

    taxable_savings_growth_rate = forms.FloatField(
        min_value=0,
        initial=6.0,
        label="Taxable Savings Growth Rate (%)",
        help_text="Expected annual growth rate for taxable savings as a percentage.",
    )

    ira_growth_rate = forms.FloatField(
        min_value=0,
        initial=6.0,
        label="IRA Growth Rate (%)",
        help_text="Expected annual growth rate for IRA savings as a percentage.",
    )

    income_pre_taxed = forms.IntegerField(
        min_value=0,
        initial=60000,
        label="Annual Pre-Tax Income",
        help_text="Your current annual income before taxes.",
    )

    target_annual_retirement_spending_pre_taxed = forms.IntegerField(
        min_value=0,
        initial=50000,
        label="Target Annual Retirement Spending (Pre-Tax)",
        help_text="Your target annual spending in retirement, before taxes.",
    )

    target_end_of_life_savings_pre_taxed = forms.IntegerField(
        min_value=0,
        initial=100000,
        label="Target End-of-Life Savings (Pre-Tax)",
        help_text="The amount you aim to have saved at the end of your life, before taxes.",
    )

    inflation_strategy = forms.ChoiceField(
        choices=INFLATION_GROWTH_STRATEGY_CHOICES,
        initial='fixed',
        label="Inflation Growth Strategy"
    )

    income_growth_strategy = forms.ChoiceField(
        choices=INCOME_GROWTH_STRATEGY_CHOICES,
        initial='fixed',
        label="Income Growth Strategy"
    )

    taxable_contribution_strategy = forms.ChoiceField(
        choices=TAXABLE_CONTRIBUTION_STRATEGY_CHOICES,
        initial='fixed',
        label="Taxable Contribution Strategy"
    )

    tax_deferred_contribution_strategy = forms.ChoiceField(
        choices=TAX_DEFERRED_CONTRIBUTION_STRATEGY_CHOICES,
        initial='fixed',
        label="Tax-Deferred Contribution Strategy"
    )

    ira_contribution_strategy = forms.ChoiceField(
        choices=IRA_CONTRIBUTION_STRATEGY_CHOICES,
        initial='fixed',
        label="Tax-Exempt Contribution Strategy"
    )

    tax_deferred_contribution_limit_inflation_rate = forms.FloatField(
        min_value=0,
        initial=2.5,
        label="Tax-Deferred Contribution Limit Inflation Rate (%)",
        help_text="Expected annual inflation rate applied to tax-deferred contribution limits.",
    )

    bank_contribution_strategy = forms.ChoiceField(
        choices=BANK_CONTRIBUTION_STRATEGY_CHOICES,
        initial='fixed',
        label="Bank Contribution Strategy"
    )

    income_growth_rate = forms.FloatField(
        min_value=0,
        initial=2.0,
        label="Income Growth Rate (%)",
        help_text="The percentage by which your income will grow annually.",
    )

    income_tax_strategy = forms.ChoiceField(
        choices=INCOME_TAX_STRATEGY_CHOICES,
        initial='simple',
        label="Income Tax Strategy"
    )

    income_tax_rate = forms.FloatField(
        min_value=0,
        max_value=100,
        initial=22.0,
        label="Income Tax Rate (%)",
        help_text="Simple flat tax rate as a percentage (used if simple tax strategy is selected).",
    )

    filing_status = forms.ChoiceField(
        choices=FILING_STATUS_CHOICES,
        initial='single',
        label="Filing Status",
        help_text="Your tax filing status.",
    )

    number_of_dependents = forms.IntegerField(
        min_value=0,
        initial=0,
        label="Number of Dependents",
        help_text="Number of qualifying dependents.",
    )

    is_blind = forms.BooleanField(
        required=False,
        initial=False,
        label="Is Blind",
        help_text="Check if you qualify for blind person's tax credit.",
    )

    employer_contribution_strategy = forms.ChoiceField(
        choices=EMPLOYER_CONTRIBUTION_STRATEGY_CHOICES,
        initial='percentage_of_contribution',
        label="Employer Contribution Strategy",
        help_text="The strategy your employer uses to contribute to your tax-deferred retirement account.",
    )

    employer_contribution_percentage = forms.FloatField(
        min_value=0,
        max_value=100,
        initial=5.0,
        label="Employer Contribution Percentage (%)",
        help_text="The percentage of your compensation that your employer contributes.",
    )

    employer_contribution_fixed_amount = forms.FloatField(
        min_value=0,
        initial=0.0,
        label="Employer Contribution Fixed Amount",
        help_text="The fixed amount your employer contributes annually.",
    )

    expenses_growth_strategy = forms.ChoiceField(
        choices=EXPENSES_GROWTH_STRATEGY_CHOICES,
        initial='fixed',
        label="Expenses Growth Strategy",
        help_text="How your expenses are expected to grow over time.",
    )

    expense_rate = forms.FloatField(
        min_value=0,
        initial=2.0,
        label="Expense Growth Rate (%)",
        help_text="The percentage by which your expenses will grow annually.",
    )

    inflation_growth_strategy = forms.ChoiceField(
        choices=INFLATION_GROWTH_STRATEGY_CHOICES,
        initial='fixed',
        label="Inflation Growth Strategy",
        help_text="How the inflation rate is expected to change over time.",
    )

    withdrawal_strategy = forms.ChoiceField(
        choices=WITHDRAWAL_STRATEGY_CHOICES,
        initial='sequential',
        label='Withdrawal Strategy',
        help_text=""
    )

    debt = forms.DecimalField(
        min_value=0,
        max_digits=12,
        decimal_places=2,
        label='Current Debt Balance',
        help_text='Enter the total amount of debt you currently owe.',
    )

    debt_interest_rate = forms.DecimalField(
        min_value=0,
        max_digits=5,
        decimal_places=2,
        label='Debt Interest Rate (%)',
        help_text='Enter the annual interest rate of your debt (as a percentage).',
    )

    debt_payment = forms.DecimalField(
        min_value=0,
        max_digits=12,
        decimal_places=2,
        label='Annual Debt Payment',
        help_text='Enter the amount you plan to pay toward your debt each year.',
    )

    # TODO Account for student loan
    # TODO Add overarching strategy for retirement
    # TODO Add Cash Maitenance Strategies
