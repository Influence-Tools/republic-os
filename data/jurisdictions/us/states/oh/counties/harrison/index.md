---
type: Jurisdiction
title: "Harrison County, OH"
classification: county
fips: "39067"
state: "OH"
demographics:
  population: 14306
  population_under_18: 3001
  population_18_64: 8041
  population_65_plus: 3264
  median_household_income: 54414
  poverty_rate: 13.1
  homeownership_rate: 76.34
  unemployment_rate: 4.55
  median_home_value: 121500
  gini_index: 0.4453
  vacancy_rate: 19.44
  race_white: 13496
  race_black: 382
  race_asian: 17
  race_native: 24
  hispanic: 167
  bachelors_plus: 1628
districts:
  - to: "us/states/oh/districts/06"
    rel: in-district
    area_weight: 0.9999
  - to: "us/states/oh/districts/senate/30"
    rel: in-district
    area_weight: 0.9998
  - to: "us/states/oh/districts/house/95"
    rel: in-district
    area_weight: 0.9997
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, oh]
timestamp: "2026-07-03"
---

# Harrison County, OH

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 14306 |
| Under 18 | 3001 |
| 18–64 | 8041 |
| 65+ | 3264 |
| Median household income | 54414 |
| Poverty rate | 13.1 |
| Homeownership rate | 76.34 |
| Unemployment rate | 4.55 |
| Median home value | 121500 |
| Gini index | 0.4453 |
| Vacancy rate | 19.44 |
| White | 13496 |
| Black | 382 |
| Asian | 17 |
| Native | 24 |
| Hispanic/Latino | 167 |
| Bachelor's or higher | 1628 |

## Districts

- [OH-06](/us/states/oh/districts/06.md) — 100% (congressional)
- [OH Senate District 30](/us/states/oh/districts/senate/30.md) — 100% (state senate)
- [OH House District 95](/us/states/oh/districts/house/95.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
