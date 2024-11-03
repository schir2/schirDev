import TaxableSavingsPipeline from "./taxableSavingsPipeline";
import TaxDeferredEmployerMatchPipeline from "./taxDeferredCompanyEmployerPipeline";
import TaxDeferredPipeline from "./taxDeferredPipeline"
import IraSavingsPipeline from "./iraSavingsPipeline";


// Initialize and export the pipeline instances directly
export const pipeline = {
    taxDeferredEmployerMatchPipeline: new TaxDeferredEmployerMatchPipeline(),
    taxableSavingsPipeline: new TaxableSavingsPipeline(),
    taxDeferredPipeline: new TaxDeferredPipeline(),
    iraSavingsPipeline: new IraSavingsPipeline(),
};