import TaxableSavingsPipeline from "./taxableSavingsPipeline";
import TaxDeferredEmployerMatchPipeline from "./taxDeferredEmployerPipeline";
import TaxDeferredPipeline from "./taxDeferredPipeline"
import IraTaxableSavingsPipeline from "./iraTaxableSavingsPipeline";
import EndOfYearPipeline from "./endOfYearPipeline";
import StartOfYearPipeline from "./startOfYearPipeline";
import IraTaxDeferredSavingsPipeline from "./iraTaxDeferredSavingsPipeline";


// Initialize and export the pipeline instances directly
export const pipeline = {
    taxDeferredEmployerMatchPipeline: new TaxDeferredEmployerMatchPipeline(),
    taxableSavingsPipeline: new TaxableSavingsPipeline(),
    taxDeferredPipeline: new TaxDeferredPipeline(),
    iraTaxableSavingsPipeline: new IraTaxableSavingsPipeline(),
    iraTaxDeferredSavingsPipeline: new IraTaxDeferredSavingsPipeline(),
    startOfYearPipeline: new StartOfYearPipeline(),
    endOfYearPipeline: new EndOfYearPipeline(),
};