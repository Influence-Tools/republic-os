---
type: Jurisdiction
title: "Elliott County, KY"
classification: county
fips: "21063"
state: "KY"
demographics:
  population: 7307
  population_under_18: 1245
  population_18_64: 4489
  population_65_plus: 1573
  median_household_income: 45776
  poverty_rate: 25.12
  homeownership_rate: 81.68
  unemployment_rate: 6.53
  median_home_value: 123500
  gini_index: 0.4478
  vacancy_rate: 20.05
  race_white: 6761
  race_black: 321
  race_asian: 0
  race_native: 15
  hispanic: 124
  bachelors_plus: 686
districts:
  - to: "us/states/ky/districts/05"
    rel: in-district
    area_weight: 1.0
  - to: "us/states/ky/districts/senate/31"
    rel: in-district
    area_weight: 0.9992
  - to: "us/states/ky/districts/house/99"
    rel: in-district
    area_weight: 0.9994
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, ky]
timestamp: "2026-07-03"
---

# Elliott County, KY

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 7307 |
| Under 18 | 1245 |
| 18–64 | 4489 |
| 65+ | 1573 |
| Median household income | 45776 |
| Poverty rate | 25.12 |
| Homeownership rate | 81.68 |
| Unemployment rate | 6.53 |
| Median home value | 123500 |
| Gini index | 0.4478 |
| Vacancy rate | 20.05 |
| White | 6761 |
| Black | 321 |
| Asian | 0 |
| Native | 15 |
| Hispanic/Latino | 124 |
| Bachelor's or higher | 686 |

## Districts

- [KY-05](/us/states/ky/districts/05.md) — 100% (congressional)
- [KY Senate District 31](/us/states/ky/districts/senate/31.md) — 100% (state senate)
- [KY House District 99](/us/states/ky/districts/house/99.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
