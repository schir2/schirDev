from django import forms


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

    TAX_EXEMPT_CONTRIBUTION_STRATEGY_CHOICES = [
        ('fixed', 'Fixed Contribution'),
        ('percent_of_income', 'Percentage of Income'),
    ]

    age = forms.IntegerField(
        min_value=0,
        max_value=100,
        initial=30,
        label="Age",
        help_text="Your current age in years.",
        widget=forms.NumberInput(attrs={'placeholder': 'e.g., 30'})
    )

    retirement_age = forms.IntegerField(
        min_value=0,
        max_value=100,
        initial=65,
        label="Retirement Age",
        help_text="The age at which you plan to retire.",
        widget=forms.NumberInput(attrs={'placeholder': 'e.g., 65'})
    )

    life_expectancy = forms.IntegerField(
        min_value=0,
        max_value=100,
        initial=85,
        label="Life Expectancy",
        help_text="Your estimated life expectancy in years.",
        widget=forms.NumberInput(attrs={'placeholder': 'e.g., 85'})
    )

    tax_deferred_savings = forms.IntegerField(
        min_value=0,
        initial=100000,
        label="Tax-Deferred Savings",
        help_text="Your current savings in tax-deferred accounts (e.g., 401(k), Traditional IRA).",
        widget=forms.NumberInput(attrs={'placeholder': 'e.g., 100000'})
    )

    taxable_savings = forms.IntegerField(
        min_value=0,
        initial=50000,
        label="Taxable Savings",
        help_text="Your current savings in taxable accounts.",
        widget=forms.NumberInput(attrs={'placeholder': 'e.g., 50000'})
    )

    tax_exempt_savings = forms.IntegerField(
        min_value=0,
        initial=30000,
        label="Tax-Exempt Savings",
        help_text="Your current savings in tax-exempt accounts (e.g., Roth IRA).",
        widget=forms.NumberInput(attrs={'placeholder': 'e.g., 30000'})
    )

    cash = forms.IntegerField(
        min_value=0,
        initial=20000,
        label="Cash",
        help_text="Your current bank savings (e.g., checking, savings accounts).",
        widget=forms.NumberInput(attrs={'placeholder': 'e.g., 20000'})
    )

    annual_taxable_contribution = forms.IntegerField(
        min_value=0,
        initial=500,
        label="Annual Taxable Contribution",
        help_text="Your annual contribution to taxable savings accounts.",
        widget=forms.NumberInput(attrs={'placeholder': 'e.g., 500'})
    )

    annual_tax_deferred_contribution = forms.IntegerField(
        min_value=0,
        initial=1000,
        label="Annual Tax-Deferred Contribution",
        help_text="Your annual contribution to tax-deferred accounts.",
        widget=forms.NumberInput(attrs={'placeholder': 'e.g., 1000'})
    )

    tax_deferred_contribution_percentage = forms.FloatField(
        min_value=0,
        max_value=100,
        initial=5.0,
        label="Tax-Deferred Contribution Percentage",
        help_text="The percentage of your pre-tax income to contribute to tax-deferred accounts.",
        widget=forms.NumberInput(attrs={'placeholder': 'e.g., 5.0', 'step': '0.1'})
    )

    tax_exempt_contribution_percentage = forms.FloatField(
        min_value=0,
        max_value=100,
        initial=5.0,
        label="Tax-Exempt Contribution Percentage",
        help_text="The percentage of your pre-tax income to contribute to tax-exempt accounts (e.g., Roth IRA).",
        widget=forms.NumberInput(attrs={'placeholder': 'e.g., 5.0', 'step': '0.1'})
    )

    taxable_contribution_percentage = forms.FloatField(
        min_value=0,
        max_value=100,
        initial=5.0,
        label="Taxable Contribution Percentage",
        help_text="The percentage of your pre-tax income to contribute to taxable accounts.",
        widget=forms.NumberInput(attrs={'placeholder': 'e.g., 5.0', 'step': '0.1'})
    )

    company_match_limit = forms.IntegerField(
        min_value=0,
        initial=5000,
        label="Company Match Limit",
        help_text="The maximum amount your company will match for tax-deferred contributions.",
        widget=forms.NumberInput(attrs={'placeholder': 'e.g., 5000'})
    )

    annual_tax_exempt_contribution = forms.IntegerField(
        min_value=0,
        initial=500,
        label="Annual Tax-Exempt Contribution",
        help_text="Your annual contribution to tax-exempt accounts (e.g., Roth IRA).",
        widget=forms.NumberInput(attrs={'placeholder': 'e.g., 500'})
    )

    annual_expenses = forms.IntegerField(
        min_value=0,
        initial=40000,
        label="Annual Expenses",
        help_text="Your estimated annual living expenses.",
        widget=forms.NumberInput(attrs={'placeholder': 'e.g., 40000'})
    )

    inflation_rate = forms.FloatField(
        min_value=0,
        initial=2.0,
        label="Inflation Rate (%)",
        help_text="Expected annual inflation rate as a percentage.",
        widget=forms.NumberInput(attrs={'placeholder': 'e.g., 2.0', 'step': '0.1'})
    )

    taxable_savings_growth_rate = forms.FloatField(
        min_value=0,
        initial=6.0,
        label="Taxable Savings Growth Rate (%)",
        help_text="Expected annual growth rate for taxable savings as a percentage.",
        widget=forms.NumberInput(attrs={'placeholder': 'e.g., 6.0', 'step': '0.1'})
    )

    tax_deferred_growth_rate = forms.FloatField(
        min_value=0,
        initial=7.0,
        label="Tax-Deferred Growth Rate (%)",
        help_text="Expected annual growth rate for tax-deferred savings as a percentage.",
        widget=forms.NumberInput(attrs={'placeholder': 'e.g., 7.0', 'step': '0.1'})
    )

    income_pre_taxed = forms.IntegerField(
        min_value=0,
        initial=60000,
        label="Annual Pre-Tax Income",
        help_text="Your current annual income before taxes.",
        widget=forms.NumberInput(attrs={'placeholder': 'e.g., 75000'})
    )

    target_annual_retirement_spending_pre_taxed = forms.IntegerField(
        min_value=0,
        initial=50000,
        label="Target Annual Retirement Spending (Pre-Tax)",
        help_text="Your target annual spending in retirement, before taxes.",
        widget=forms.NumberInput(attrs={'placeholder': 'e.g., 50000'})
    )

    target_end_of_life_savings_pre_taxed = forms.IntegerField(
        min_value=0,
        initial=100000,
        label="Target End-of-Life Savings (Pre-Tax)",
        help_text="The amount you aim to have saved at the end of your life, before taxes.",
        widget=forms.NumberInput(attrs={'placeholder': 'e.g., 100000'})
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

    tax_exempt_contribution_strategy = forms.ChoiceField(
        choices=TAX_EXEMPT_CONTRIBUTION_STRATEGY_CHOICES,
        initial='fixed',
        label="Tax-Exempt Contribution Strategy"
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
        widget=forms.NumberInput(attrs={'placeholder': 'e.g., 2.0', 'step': '0.1'})
    )
