---
type: Jurisdiction
title: "Cape May County, NJ"
classification: county
fips: "34009"
state: "NJ"
demographics:
  population: 94941
  population_under_18: 16274
  population_18_64: 50659
  population_65_plus: 28008
  median_household_income: 91128
  poverty_rate: 8.73
  homeownership_rate: 80.32
  unemployment_rate: 5.27
  median_home_value: 434600
  gini_index: 0.4598
  vacancy_rate: 54.94
  race_white: 80838
  race_black: 3529
  race_asian: 687
  race_native: 354
  hispanic: 7854
  bachelors_plus: 39202
districts:
  - to: "us/states/nj/districts/02"
    rel: in-district
    area_weight: 0.459
  - to: "us/states/nj/districts/senate/1"
    rel: in-district
    area_weight: 0.4585
  - to: "us/states/nj/districts/house/1"
    rel: in-district
    area_weight: 0.4585
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, nj]
timestamp: "2026-07-03"
---

# Cape May County, NJ

County jurisdiction — 2 officeholders mapped.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 94941 |
| Under 18 | 16274 |
| 18–64 | 50659 |
| 65+ | 28008 |
| Median household income | 91128 |
| Poverty rate | 8.73 |
| Homeownership rate | 80.32 |
| Unemployment rate | 5.27 |
| Median home value | 434600 |
| Gini index | 0.4598 |
| Vacancy rate | 54.94 |
| White | 80838 |
| Black | 3529 |
| Asian | 687 |
| Native | 354 |
| Hispanic/Latino | 7854 |
| Bachelor's or higher | 39202 |

## Districts

- [NJ-02](/us/states/nj/districts/02.md) — 46% (congressional)
- [NJ Senate District 1](/us/states/nj/districts/senate/1.md) — 46% (state senate)
- [NJ House District 1](/us/states/nj/districts/house/1.md) — 46% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
