export const CONTRIBUTION_LIMITS_401K_BY_YEAR: {
  [year: number]: {
    electiveDeferralLimit: number;
    catchUpContributionLimit: number;
    totalContributionLimit: number;
  };
} = {
  2021: {
    electiveDeferralLimit: 19500,
    catchUpContributionLimit: 6500,
    totalContributionLimit: 58000,
  },
  2022: {
    electiveDeferralLimit: 20500,
    catchUpContributionLimit: 6500,
    totalContributionLimit: 61000,
  },
  2023: {
    electiveDeferralLimit: 20500,
    catchUpContributionLimit: 6500,
    totalContributionLimit: 61000,
  },
  2024: {
    electiveDeferralLimit: 22500,
    catchUpContributionLimit: 7500,
    totalContributionLimit: 66000,
  },
  // Add more years as needed
};
export const INFLATION_ROUNDING_INCREMENT = 500