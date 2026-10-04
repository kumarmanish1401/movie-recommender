# Simple Movie Recommender
MSAI-631 Week 6. A basic adaptation of the course-provided movie recommender.
One movie dropdown, one optional genre filter, one Recommend button, one results table.

## Run (Python 3.10+)
```sh
python -m venv .venv
```
Windows: `.venv\Scripts\activate`
macOS/Linux: `source .venv/bin/activate`
```sh
python -m pip install -r requirements.txt
python app.py
```
Open http://127.0.0.1:5000 ; stop with Ctrl+C.
No API key, accounts, extra dataset download or AI service required.

## Understand the code
movies.csv -> genre counts -> cosine similarity -> sorted matches -> optional filter.
Select Toy Story: Finding Nemo and Finding Dory should appear before different-genre items.
Select Toy Story with Crime: no positive-similarity matching candidate exists.
Equal scores keep CSV order. There can be fewer than five matches.
The genre labels are simplified educational annotations, not official IMDb metadata.
Genre similarity does not measure probability of enjoyment or movie quality.

## Checks
```sh
python -m unittest discover -s tests -v
```
See TEST_RESULTS.txt. Human usability and actual preference accuracy have not been measured.

## GitHub and submission
Suggested repository name: msai631-simple-movie-recommender.
No live repository URL has been created.
1. Run the app and review the code and report.
2. Create this repository on GitHub and upload all files, retaining templates/ and tests/.
3. Copy its actual URL into the report's repository field.
4. If private, add your instructor's verified GitHub username under Settings > Collaborators.
5. Confirm instructor access, fill in title-page details, and submit DOCX plus ZIP.
Do not substitute the foundation repository URL for your own.
See ATTRIBUTION.md and LICENSE for credit. Flask's local server is for development only.
