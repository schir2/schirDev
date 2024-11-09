import {calculateCompoundInterest} from "./financial";
import {
    TAX_DEFERRED_CONTRIBUTION_LIMIT_2024,
    TAX_DEFERRED_DEFAULT_YEAR,
    TAX_DEFERRED_ELECTIVE_CONTRIBUTION_CATCH_UP_LIMIT_2024,
    TAX_DEFERRED_ELECTIVE_CONTRIBUTION_LIMIT_2024,
    TAX_DEFERRED_LIMIT_INFLATION_RATE
} from "../constants";


export function calculateTaxDeferredContributionLimit(year: number): number {
    return calculateCompoundInterest(
        TAX_DEFERRED_CONTRIBUTION_LIMIT_2024,
        TAX_DEFERRED_LIMIT_INFLATION_RATE / 100,
        1,
        year - TAX_DEFERRED_DEFAULT_YEAR
    )

}

export function calculateTaxDeferredElectiveContributionLimit(year: number): number {
    return calculateCompoundInterest(
        TAX_DEFERRED_ELECTIVE_CONTRIBUTION_LIMIT_2024,
        TAX_DEFERRED_LIMIT_INFLATION_RATE / 100,
        1,
        year - TAX_DEFERRED_DEFAULT_YEAR
    )

}

export function calculateTaxDeferredElectiveContributionCatchUpLimit(year: number): number {
    return calculateCompoundInterest(
        TAX_DEFERRED_ELECTIVE_CONTRIBUTION_CATCH_UP_LIMIT_2024,
        TAX_DEFERRED_LIMIT_INFLATION_RATE / 100,
        1,
        year - TAX_DEFERRED_DEFAULT_YEAR
    )

}