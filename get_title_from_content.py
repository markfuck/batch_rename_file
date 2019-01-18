"""
@author: majb
@date: 2019/1/18
@file: get_title_from_content.py
"""
from pdfminer.pdfparser import PDFParser, PDFDocument
from pdfminer.pdfinterp import PDFTextExtractionNotAllowed, PDFResourceManager, PDFPageInterpreter
from pdfminer.layout import LTTextBoxHorizontal, LAParams
from pdfminer.converter import PDFPageAggregator


def read_content():
    with open("file/10.1016@j.burns.2016.01.025.pdf", "rb") as f:
        parser = PDFParser(f)
        doc = PDFDocument()
        parser.set_document(doc)
        doc.set_parser(parser)

        doc.initialize()

        if not doc.is_extractable:
            raise PDFTextExtractionNotAllowed
        else:
            pdf_manager = PDFResourceManager()
            laParams = LAParams()
            device = PDFPageAggregator(pdf_manager, laparams=laParams)
            interpreter = PDFPageInterpreter(pdf_manager, device)
            for page in doc.get_pages():
                interpreter.process_page(page)
                layout = device.get_result()
                for x in layout:
                    if isinstance(x, LTTextBoxHorizontal):
                        print(x.get_text())


if __name__ == '__main__':
    read_content()
