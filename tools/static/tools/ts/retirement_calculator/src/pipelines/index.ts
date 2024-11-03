import TaxableSavingsPipeline from "/pipelines/taxableSavingsPipeline";
import TaxDeferredCompanyMatchPipeline from "/pipelines/taxDeferredCompanyMatchPipeline";
import TaxDeferredSupplementalPipeline from "/pipelines/taxDeferredSupplementalPipeline"


// Initialize and export the pipeline instances directly
export const pipelines = {
    taxDeferredCompanyMatchPipeline: new TaxDeferredCompanyMatchPipeline(),
    taxableSavings: new TaxableSavingsPipeline(),
    taxDeferredSupplementalPipeline: new TaxDeferredSupplementalPipeline()
};