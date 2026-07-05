---
type: Jurisdiction
title: "San Jacinto County, TX"
classification: county
fips: "48407"
state: "TX"
demographics:
  population: 28441
  population_under_18: 6120
  population_18_64: 16191
  population_65_plus: 6130
  median_household_income: 65364
  poverty_rate: 18.37
  homeownership_rate: 84.56
  unemployment_rate: 6.77
  median_home_value: 209300
  gini_index: 0.4362
  vacancy_rate: 27.51
  race_white: 20618
  race_black: 2504
  race_asian: 98
  race_native: 164
  hispanic: 5452
  bachelors_plus: 4550
districts:
  - to: "us/states/tx/districts/08"
    rel: in-district
    area_weight: 0.9985
  - to: "us/states/tx/districts/senate/5"
    rel: in-district
    area_weight: 0.9997
  - to: "us/states/tx/districts/house/18"
    rel: in-district
    area_weight: 0.9997
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, tx]
timestamp: "2026-07-03"
---

# San Jacinto County, TX

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 28441 |
| Under 18 | 6120 |
| 18–64 | 16191 |
| 65+ | 6130 |
| Median household income | 65364 |
| Poverty rate | 18.37 |
| Homeownership rate | 84.56 |
| Unemployment rate | 6.77 |
| Median home value | 209300 |
| Gini index | 0.4362 |
| Vacancy rate | 27.51 |
| White | 20618 |
| Black | 2504 |
| Asian | 98 |
| Native | 164 |
| Hispanic/Latino | 5452 |
| Bachelor's or higher | 4550 |

## Districts

- [TX-08](/us/states/tx/districts/08.md) — 100% (congressional)
- [TX Senate District 5](/us/states/tx/districts/senate/5.md) — 100% (state senate)
- [TX House District 18](/us/states/tx/districts/house/18.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
