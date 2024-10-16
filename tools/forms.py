from django import forms


class RetirementCalculatorForm(forms.Form):
    current_age = forms.IntegerField(
        min_value=0,
        max_value=100,
        initial=30,
        label="Current Age",
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

    current_tax_deferred_savings = forms.IntegerField(
        min_value=0,
        initial=100000,
        label="Current Tax-Deferred Savings",
        help_text="Your current savings in tax-deferred accounts (e.g., 401(k), Traditional IRA).",
        widget=forms.NumberInput(attrs={'placeholder': 'e.g., 100000'})
    )

    current_taxable_savings = forms.IntegerField(
        min_value=0,
        initial=50000,
        label="Current Taxable Savings",
        help_text="Your current savings in taxable accounts.",
        widget=forms.NumberInput(attrs={'placeholder': 'e.g., 50000'})
    )

    current_tax_exempt_savings = forms.IntegerField(
        min_value=0,
        initial=30000,
        label="Current Tax-Exempt Savings",
        help_text="Your current savings in tax-exempt accounts (e.g., Roth IRA).",
        widget=forms.NumberInput(attrs={'placeholder': 'e.g., 30000'})
    )

    current_bank_savings = forms.IntegerField(
        min_value=0,
        initial=20000,
        label="Current Bank Savings",
        help_text="Your current bank savings (e.g., checking, savings accounts).",
        widget=forms.NumberInput(attrs={'placeholder': 'e.g., 20000'})
    )

    monthly_taxable_contribution = forms.IntegerField(
        min_value=0,
        initial=500,
        label="Monthly Taxable Contribution",
        help_text="Your monthly contribution to taxable savings accounts.",
        widget=forms.NumberInput(attrs={'placeholder': 'e.g., 500'})
    )

    monthly_tax_deferred_contribution = forms.IntegerField(
        min_value=0,
        initial=1000,
        label="Monthly Tax-Deferred Contribution",
        help_text="Your monthly contribution to tax-deferred accounts.",
        widget=forms.NumberInput(attrs={'placeholder': 'e.g., 1000'})
    )

    monthly_tax_exempt_contribution = forms.IntegerField(
        min_value=0,
        initial=500,
        label="Monthly Tax-Exempt Contribution",
        help_text="Your monthly contribution to tax-exempt accounts (e.g., Roth IRA).",
        widget=forms.NumberInput(attrs={'placeholder': 'e.g., 500'})
    )

    monthly_bank_contribution = forms.IntegerField(
        min_value=0,
        initial=200,
        label="Monthly Bank Savings Contribution",
        help_text="Your monthly contribution to bank savings accounts.",
        widget=forms.NumberInput(attrs={'placeholder': 'e.g., 200'})
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

    annual_earning_pre_taxed = forms.IntegerField(
        min_value=0,
        initial=75000,
        label="Annual Pre-Tax Earnings",
        help_text="Your current annual earnings before taxes.",
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
