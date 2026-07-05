---
type: Jurisdiction
title: "Phillips County, MT"
classification: county
fips: "30071"
state: "MT"
demographics:
  population: 4221
  population_under_18: 987
  population_18_64: 2221
  population_65_plus: 1013
  median_household_income: 53417
  poverty_rate: 10.52
  homeownership_rate: 73.54
  unemployment_rate: 1.79
  median_home_value: 197600
  gini_index: 0.4267
  vacancy_rate: 20.96
  race_white: 3425
  race_black: 34
  race_asian: 34
  race_native: 316
  hispanic: 46
  bachelors_plus: 963
districts:
  - to: "us/states/mt/districts/02"
    rel: in-district
    area_weight: 1.0
  - to: "us/states/mt/districts/senate/16"
    rel: in-district
    area_weight: 0.6133
  - to: "us/states/mt/districts/senate/14"
    rel: in-district
    area_weight: 0.3867
  - to: "us/states/mt/districts/house/28"
    rel: in-district
    area_weight: 0.3867
  - to: "us/states/mt/districts/house/31"
    rel: in-district
    area_weight: 0.3197
  - to: "us/states/mt/districts/house/32"
    rel: in-district
    area_weight: 0.2935
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, mt]
timestamp: "2026-07-03"
---

# Phillips County, MT

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 4221 |
| Under 18 | 987 |
| 18–64 | 2221 |
| 65+ | 1013 |
| Median household income | 53417 |
| Poverty rate | 10.52 |
| Homeownership rate | 73.54 |
| Unemployment rate | 1.79 |
| Median home value | 197600 |
| Gini index | 0.4267 |
| Vacancy rate | 20.96 |
| White | 3425 |
| Black | 34 |
| Asian | 34 |
| Native | 316 |
| Hispanic/Latino | 46 |
| Bachelor's or higher | 963 |

## Districts

- [MT-02](/us/states/mt/districts/02.md) — 100% (congressional)
- [MT Senate District 16](/us/states/mt/districts/senate/16.md) — 61% (state senate)
- [MT Senate District 14](/us/states/mt/districts/senate/14.md) — 39% (state senate)
- [MT House District 28](/us/states/mt/districts/house/28.md) — 39% (state house)
- [MT House District 31](/us/states/mt/districts/house/31.md) — 32% (state house)
- [MT House District 32](/us/states/mt/districts/house/32.md) — 29% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
