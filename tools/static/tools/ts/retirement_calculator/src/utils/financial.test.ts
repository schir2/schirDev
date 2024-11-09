import { describe, it, expect } from 'vitest';
import { calculateCompoundInterest } from './financial';

describe('calculateCompoundInterest', () => {
  it('calculates compound interest correctly for annual compounding', () => {
    const result = calculateCompoundInterest(1000, 0.05, 1, 10);
    expect(result).toBeCloseTo(1628.89, 2); // Validate up to two decimal places
  });

  it('calculates compound interest correctly for monthly compounding', () => {
    const result = calculateCompoundInterest(1000, 0.05, 12, 10);
    expect(result).toBeCloseTo(1647.01, 2); // Validate up to two decimal places
  });

  it('returns the principal when interest rate and periods are zero', () => {
    const result = calculateCompoundInterest(1000, 0, 1, 0);
    expect(result).toBe(1000);
  });

  it('handles edge cases like zero principal', () => {
    const result = calculateCompoundInterest(0, 0.05, 1, 10);
    expect(result).toBe(0);
  });
});
