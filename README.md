# CertiflixUI

# Final PPT also attached

Creating a specialized solution for evaluating the accuracy and quality of product images on various marketplace and e-commerce platforms is imperative. As online shopping increasingly relies on visual content, ensuring the correctness and authenticity of these images is paramount for establishing trust and aiding consumers in making informed purchasing decisions.

Image correctness analysis involves automatically assessing the precision, completeness, and relevance of product visuals showcased on online marketplaces and e-commerce platforms. Its objective is to identify potential issues like misleading representations, altered visuals, or discrepancies in product details.

We employ two primary approaches to accomplish this task:

A web extension designed to authenticate products on other e-commerce platforms. This extension verifies product authenticity during each purchase process on external websites. Utilizing web scraping techniques, it retrieves images from existing websites and subjects them to scrutiny using our product identifier model, logo detector model, and text extraction capabilities. Deep learning models and natural language processing techniques aid in this analysis. Ultimately, the extension provides a percentage-based assessment of image correctness. If the value falls below a predefined threshold, the product image is flagged as potentially counterfeit.

An e-commerce platform where sellers can upload high-quality product images that undergo similar authenticity checks. Flask Server handles the backend processes, while Firebase stores seller information on the website.

These measures ensure that product images meet stringent quality standards, fostering consumer trust and confidence in online transactions.
