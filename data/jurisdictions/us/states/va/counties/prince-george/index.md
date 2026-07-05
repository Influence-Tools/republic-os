---
type: Jurisdiction
title: "Prince George County, VA"
classification: county
fips: "51149"
state: "VA"
demographics:
  population: 43146
  population_under_18: 8419
  population_18_64: 29030
  population_65_plus: 5697
  median_household_income: 84897
  poverty_rate: 8.89
  homeownership_rate: 74.35
  unemployment_rate: 5.21
  median_home_value: 293400
  gini_index: 0.3786
  vacancy_rate: 4.53
  race_white: 23235
  race_black: 13557
  race_asian: 801
  race_native: 267
  hispanic: 4487
  bachelors_plus: 9259
districts:
  - to: "us/states/va/districts/04"
    rel: in-district
    area_weight: 1.0
  - to: "us/states/va/districts/senate/13"
    rel: in-district
    area_weight: 1.0
  - to: "us/states/va/districts/house/82"
    rel: in-district
    area_weight: 0.872
  - to: "us/states/va/districts/house/75"
    rel: in-district
    area_weight: 0.1278
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, va]
timestamp: "2026-07-03"
---

# Prince George County, VA

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 43146 |
| Under 18 | 8419 |
| 18–64 | 29030 |
| 65+ | 5697 |
| Median household income | 84897 |
| Poverty rate | 8.89 |
| Homeownership rate | 74.35 |
| Unemployment rate | 5.21 |
| Median home value | 293400 |
| Gini index | 0.3786 |
| Vacancy rate | 4.53 |
| White | 23235 |
| Black | 13557 |
| Asian | 801 |
| Native | 267 |
| Hispanic/Latino | 4487 |
| Bachelor's or higher | 9259 |

## Districts

- [VA-04](/us/states/va/districts/04.md) — 100% (congressional)
- [VA Senate District 13](/us/states/va/districts/senate/13.md) — 100% (state senate)
- [VA House District 82](/us/states/va/districts/house/82.md) — 87% (state house)
- [VA House District 75](/us/states/va/districts/house/75.md) — 13% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
