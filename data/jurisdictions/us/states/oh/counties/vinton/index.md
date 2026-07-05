---
type: Jurisdiction
title: "Vinton County, OH"
classification: county
fips: "39163"
state: "OH"
demographics:
  population: 12630
  population_under_18: 2625
  population_18_64: 7528
  population_65_plus: 2477
  median_household_income: 55336
  poverty_rate: 17.28
  homeownership_rate: 75.53
  unemployment_rate: 5.53
  median_home_value: 150000
  gini_index: 0.4353
  vacancy_rate: 10.23
  race_white: 12129
  race_black: 128
  race_asian: 183
  race_native: 0
  hispanic: 25
  bachelors_plus: 1646
districts:
  - to: "us/states/oh/districts/02"
    rel: in-district
    area_weight: 1.0
  - to: "us/states/oh/districts/senate/17"
    rel: in-district
    area_weight: 1.0
  - to: "us/states/oh/districts/house/92"
    rel: in-district
    area_weight: 1.0
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, oh]
timestamp: "2026-07-03"
---

# Vinton County, OH

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 12630 |
| Under 18 | 2625 |
| 18–64 | 7528 |
| 65+ | 2477 |
| Median household income | 55336 |
| Poverty rate | 17.28 |
| Homeownership rate | 75.53 |
| Unemployment rate | 5.53 |
| Median home value | 150000 |
| Gini index | 0.4353 |
| Vacancy rate | 10.23 |
| White | 12129 |
| Black | 128 |
| Asian | 183 |
| Native | 0 |
| Hispanic/Latino | 25 |
| Bachelor's or higher | 1646 |

## Districts

- [OH-02](/us/states/oh/districts/02.md) — 100% (congressional)
- [OH Senate District 17](/us/states/oh/districts/senate/17.md) — 100% (state senate)
- [OH House District 92](/us/states/oh/districts/house/92.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
