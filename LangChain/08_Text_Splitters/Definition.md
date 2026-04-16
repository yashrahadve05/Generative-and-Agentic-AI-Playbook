## **Text Splitters:** Text Splitters are tools that break down large pieces of text into smaller, more manageable chunks. This is particularly useful in natural language processing (NLP) tasks, where handling large texts can be computationally expensive and inefficient. By splitting text into smaller segments, we can improve the performance of various NLP applications, such as text classification, sentiment analysis, and language modeling.

#### **Text Splitting:** "Text Splitting is the process of breaking large chunks of text (like articles, PDFs, HTML page, or books) into smaller, manageable pieces(chunks) that an LLM can handle effectively". This is crucial for tasks that involve processing large documents, as it allows for better performance and more accurate results. Text splitting can be done based on various criteria, such as sentence boundaries, paragraph breaks, or specific delimiters.

#### **Text Splitter Types:**
1. **Character-based Splitters:** These split text based on a specific number of characters. For example, a character-based splitter might break text into chunks of 500 characters each.
2. **Sentence-based Splitters:** These split text based on sentence boundaries. This is often done using natural language processing techniques to identify where sentences end, ensuring that chunks are coherent and meaningful.
3. **Paragraph-based Splitters:** These split text based on paragraph breaks. This is useful for documents that are structured with clear paragraph divisions, allowing for more contextually relevant chunks.
4. **Custom Delimiter Splitters:** These split text based on specific delimiters defined by the user. For example, a custom delimiter splitter might break text at specific keywords or symbols that are relevant to the task at hand.
5. **Recursive Splitters:** These split text recursively, meaning that if a chunk exceeds a certain size, it will be further split until it meets the desired size criteria. This is particularly useful for handling very large documents.
6. **Token-based Splitters:** These split text based on a specific number of tokens, which can be more effective than character-based splitting for certain NLP tasks, as it takes into account the actual words and their meanings rather than just the number of characters.
7. **Semantic Splitters:** These split text based on semantic meaning, using techniques like topic modeling or clustering to group related sentences or paragraphs together. This can help preserve the context and improve the relevance of the chunks for specific NLP tasks.


## **Text Splitter**
- Length Based
- Text Structure Based : Widely Used
- Document Structure Based
    1. Python Code Splitter
    2. Markdown Code Splitter
- Semantic Meaning Based