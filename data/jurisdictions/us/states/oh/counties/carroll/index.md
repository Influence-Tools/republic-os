---
type: Jurisdiction
title: "Carroll County, OH"
classification: county
fips: "39019"
state: "OH"
demographics:
  population: 26659
  population_under_18: 5450
  population_18_64: 15255
  population_65_plus: 5954
  median_household_income: 64835
  poverty_rate: 12.85
  homeownership_rate: 78.72
  unemployment_rate: 5.63
  median_home_value: 183100
  gini_index: 0.4306
  vacancy_rate: 16.31
  race_white: 25228
  race_black: 195
  race_asian: 9
  race_native: 19
  hispanic: 355
  bachelors_plus: 4327
districts:
  - to: "us/states/oh/districts/06"
    rel: in-district
    area_weight: 1.0
  - to: "us/states/oh/districts/senate/33"
    rel: in-district
    area_weight: 0.9999
  - to: "us/states/oh/districts/house/79"
    rel: in-district
    area_weight: 0.9999
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, oh]
timestamp: "2026-07-03"
---

# Carroll County, OH

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 26659 |
| Under 18 | 5450 |
| 18–64 | 15255 |
| 65+ | 5954 |
| Median household income | 64835 |
| Poverty rate | 12.85 |
| Homeownership rate | 78.72 |
| Unemployment rate | 5.63 |
| Median home value | 183100 |
| Gini index | 0.4306 |
| Vacancy rate | 16.31 |
| White | 25228 |
| Black | 195 |
| Asian | 9 |
| Native | 19 |
| Hispanic/Latino | 355 |
| Bachelor's or higher | 4327 |

## Districts

- [OH-06](/us/states/oh/districts/06.md) — 100% (congressional)
- [OH Senate District 33](/us/states/oh/districts/senate/33.md) — 100% (state senate)
- [OH House District 79](/us/states/oh/districts/house/79.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
