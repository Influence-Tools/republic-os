---
type: Jurisdiction
title: "Clark County, OH"
classification: county
fips: "39023"
state: "OH"
demographics:
  population: 135158
  population_under_18: 30519
  population_18_64: 77234
  population_65_plus: 27405
  median_household_income: 63132
  poverty_rate: 15.19
  homeownership_rate: 69.4
  unemployment_rate: 6.71
  median_home_value: 169900
  gini_index: 0.4332
  vacancy_rate: 8.43
  race_white: 111360
  race_black: 10868
  race_asian: 814
  race_native: 156
  hispanic: 5733
  bachelors_plus: 25936
districts:
  - to: "us/states/oh/districts/15"
    rel: in-district
    area_weight: 0.7099
  - to: "us/states/oh/districts/10"
    rel: in-district
    area_weight: 0.2899
  - to: "us/states/oh/districts/senate/10"
    rel: in-district
    area_weight: 0.9997
  - to: "us/states/oh/districts/house/74"
    rel: in-district
    area_weight: 0.598
  - to: "us/states/oh/districts/house/71"
    rel: in-district
    area_weight: 0.4018
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, oh]
timestamp: "2026-07-03"
---

# Clark County, OH

County jurisdiction — 1 officeholders mapped.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 135158 |
| Under 18 | 30519 |
| 18–64 | 77234 |
| 65+ | 27405 |
| Median household income | 63132 |
| Poverty rate | 15.19 |
| Homeownership rate | 69.4 |
| Unemployment rate | 6.71 |
| Median home value | 169900 |
| Gini index | 0.4332 |
| Vacancy rate | 8.43 |
| White | 111360 |
| Black | 10868 |
| Asian | 814 |
| Native | 156 |
| Hispanic/Latino | 5733 |
| Bachelor's or higher | 25936 |

## Districts

- [OH-15](/us/states/oh/districts/15.md) — 71% (congressional)
- [OH-10](/us/states/oh/districts/10.md) — 29% (congressional)
- [OH Senate District 10](/us/states/oh/districts/senate/10.md) — 100% (state senate)
- [OH House District 74](/us/states/oh/districts/house/74.md) — 60% (state house)
- [OH House District 71](/us/states/oh/districts/house/71.md) — 40% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
