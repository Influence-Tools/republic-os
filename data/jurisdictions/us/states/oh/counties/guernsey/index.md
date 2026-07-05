---
type: Jurisdiction
title: "Guernsey County, OH"
classification: county
fips: "39059"
state: "OH"
demographics:
  population: 38223
  population_under_18: 8455
  population_18_64: 22104
  population_65_plus: 7664
  median_household_income: 58478
  poverty_rate: 15.31
  homeownership_rate: 72.1
  unemployment_rate: 5.25
  median_home_value: 157700
  gini_index: 0.4383
  vacancy_rate: 14.28
  race_white: 35860
  race_black: 754
  race_asian: 132
  race_native: 9
  hispanic: 519
  bachelors_plus: 5707
districts:
  - to: "us/states/oh/districts/12"
    rel: in-district
    area_weight: 0.9994
  - to: "us/states/oh/districts/senate/30"
    rel: in-district
    area_weight: 0.5373
  - to: "us/states/oh/districts/senate/31"
    rel: in-district
    area_weight: 0.4626
  - to: "us/states/oh/districts/house/95"
    rel: in-district
    area_weight: 0.5373
  - to: "us/states/oh/districts/house/97"
    rel: in-district
    area_weight: 0.4626
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, oh]
timestamp: "2026-07-03"
---

# Guernsey County, OH

County jurisdiction — 1 officeholders mapped.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 38223 |
| Under 18 | 8455 |
| 18–64 | 22104 |
| 65+ | 7664 |
| Median household income | 58478 |
| Poverty rate | 15.31 |
| Homeownership rate | 72.1 |
| Unemployment rate | 5.25 |
| Median home value | 157700 |
| Gini index | 0.4383 |
| Vacancy rate | 14.28 |
| White | 35860 |
| Black | 754 |
| Asian | 132 |
| Native | 9 |
| Hispanic/Latino | 519 |
| Bachelor's or higher | 5707 |

## Districts

- [OH-12](/us/states/oh/districts/12.md) — 100% (congressional)
- [OH Senate District 30](/us/states/oh/districts/senate/30.md) — 54% (state senate)
- [OH Senate District 31](/us/states/oh/districts/senate/31.md) — 46% (state senate)
- [OH House District 95](/us/states/oh/districts/house/95.md) — 54% (state house)
- [OH House District 97](/us/states/oh/districts/house/97.md) — 46% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
