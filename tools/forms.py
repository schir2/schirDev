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
        ('percent_of_income', 'Percentage of Income'),
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
        ('until_company_match', 'Until Company Match Met'),
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

    age = forms.IntegerField(
        min_value=0,
        max_value=100,
        initial=30,
        label="Age",
        help_text="Your current age in years.",
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

    annual_taxable_contribution = forms.IntegerField(
        min_value=0,
        initial=500,
        label="Annual Taxable Contribution",
        help_text="Your annual contribution to taxable savings accounts.",
    )

    annual_tax_deferred_contribution = forms.IntegerField(
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

    company_match_limit = forms.IntegerField(
        min_value=0,
        initial=5000,
        label="Company Match Limit",
        help_text="The maximum amount your company will match for tax-deferred contributions.",
    )

    company_match_percentage = forms.IntegerField(
        min_value=0,
        initial=100,
        label="Company Match Percentage",
        help_text="The percentage at which your company will match for tax-deferred contributions.",
    )

    annual_ira_contribution = forms.IntegerField(
        min_value=0,
        initial=500,
        label="Annual Tax-Exempt Contribution",
        help_text="Your annual contribution to tax-exempt accounts (e.g., Roth IRA).",
    )

    annual_expenses = forms.IntegerField(
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

    tax_deferred_growth_rate = forms.FloatField(
        min_value=0,
        initial=7.0,
        label="Tax-Deferred Growth Rate (%)",
        help_text="Expected annual growth rate for tax-deferred savings as a percentage.",
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
        label="Tax-Deferred Growth Rate (%)",
        help_text="Expected annual inflation rate as a percentage.",
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
