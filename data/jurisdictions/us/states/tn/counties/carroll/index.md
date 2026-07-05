---
type: Jurisdiction
title: "Carroll County, TN"
classification: county
fips: "47017"
state: "TN"
demographics:
  population: 28641
  population_under_18: 7153
  population_18_64: 8428
  population_65_plus: 13060
  median_household_income: 51787
  poverty_rate: 16.96
  homeownership_rate: 74.54
  unemployment_rate: 4.52
  median_home_value: 142400
  gini_index: 0.4363
  vacancy_rate: 11.9
  race_white: 24195
  race_black: 2415
  race_asian: 87
  race_native: 33
  hispanic: 899
  bachelors_plus: 5007
districts:
  - to: "us/states/tn/districts/08"
    rel: in-district
    area_weight: 1.0
  - to: "us/states/tn/districts/senate/24"
    rel: in-district
    area_weight: 0.9999
  - to: "us/states/tn/districts/house/79"
    rel: in-district
    area_weight: 0.656
  - to: "us/states/tn/districts/house/76"
    rel: in-district
    area_weight: 0.3438
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, tn]
timestamp: "2026-07-03"
---

# Carroll County, TN

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 28641 |
| Under 18 | 7153 |
| 18–64 | 8428 |
| 65+ | 13060 |
| Median household income | 51787 |
| Poverty rate | 16.96 |
| Homeownership rate | 74.54 |
| Unemployment rate | 4.52 |
| Median home value | 142400 |
| Gini index | 0.4363 |
| Vacancy rate | 11.9 |
| White | 24195 |
| Black | 2415 |
| Asian | 87 |
| Native | 33 |
| Hispanic/Latino | 899 |
| Bachelor's or higher | 5007 |

## Districts

- [TN-08](/us/states/tn/districts/08.md) — 100% (congressional)
- [TN Senate District 24](/us/states/tn/districts/senate/24.md) — 100% (state senate)
- [TN House District 79](/us/states/tn/districts/house/79.md) — 66% (state house)
- [TN House District 76](/us/states/tn/districts/house/76.md) — 34% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
