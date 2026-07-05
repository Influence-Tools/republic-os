---
type: Jurisdiction
title: "Ocean County, NJ"
classification: county
fips: "34029"
state: "NJ"
demographics:
  population: 654362
  population_under_18: 163366
  population_18_64: 342989
  population_65_plus: 148007
  median_household_income: 89863
  poverty_rate: 10.5
  homeownership_rate: 80.74
  unemployment_rate: 5.45
  median_home_value: 398400
  gini_index: 0.4499
  vacancy_rate: 17.72
  race_white: 545002
  race_black: 19905
  race_asian: 12621
  race_native: 2587
  hispanic: 71391
  bachelors_plus: 207710
districts:
  - to: "us/states/nj/districts/04"
    rel: in-district
    area_weight: 0.5266
  - to: "us/states/nj/districts/02"
    rel: in-district
    area_weight: 0.2985
  - to: "us/states/nj/districts/senate/9"
    rel: in-district
    area_weight: 0.5375
  - to: "us/states/nj/districts/senate/12"
    rel: in-district
    area_weight: 0.1536
  - to: "us/states/nj/districts/senate/10"
    rel: in-district
    area_weight: 0.1059
  - to: "us/states/nj/districts/senate/30"
    rel: in-district
    area_weight: 0.0275
  - to: "us/states/nj/districts/house/9"
    rel: in-district
    area_weight: 0.5375
  - to: "us/states/nj/districts/house/12"
    rel: in-district
    area_weight: 0.1536
  - to: "us/states/nj/districts/house/10"
    rel: in-district
    area_weight: 0.1059
  - to: "us/states/nj/districts/house/30"
    rel: in-district
    area_weight: 0.0275
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, nj]
timestamp: "2026-07-03"
---

# Ocean County, NJ

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 654362 |
| Under 18 | 163366 |
| 18–64 | 342989 |
| 65+ | 148007 |
| Median household income | 89863 |
| Poverty rate | 10.5 |
| Homeownership rate | 80.74 |
| Unemployment rate | 5.45 |
| Median home value | 398400 |
| Gini index | 0.4499 |
| Vacancy rate | 17.72 |
| White | 545002 |
| Black | 19905 |
| Asian | 12621 |
| Native | 2587 |
| Hispanic/Latino | 71391 |
| Bachelor's or higher | 207710 |

## Districts

- [NJ-04](/us/states/nj/districts/04.md) — 53% (congressional)
- [NJ-02](/us/states/nj/districts/02.md) — 30% (congressional)
- [NJ Senate District 9](/us/states/nj/districts/senate/9.md) — 54% (state senate)
- [NJ Senate District 12](/us/states/nj/districts/senate/12.md) — 15% (state senate)
- [NJ Senate District 10](/us/states/nj/districts/senate/10.md) — 11% (state senate)
- [NJ Senate District 30](/us/states/nj/districts/senate/30.md) — 3% (state senate)
- [NJ House District 9](/us/states/nj/districts/house/9.md) — 54% (state house)
- [NJ House District 12](/us/states/nj/districts/house/12.md) — 15% (state house)
- [NJ House District 10](/us/states/nj/districts/house/10.md) — 11% (state house)
- [NJ House District 30](/us/states/nj/districts/house/30.md) — 3% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
