---
type: Jurisdiction
title: "Hamilton County, TN"
classification: county
fips: "47065"
state: "TN"
demographics:
  population: 376192
  population_under_18: 79311
  population_18_64: 227795
  population_65_plus: 69086
  median_household_income: 76183
  poverty_rate: 13.08
  homeownership_rate: 63.91
  unemployment_rate: 4.37
  median_home_value: 312800
  gini_index: 0.485
  vacancy_rate: 8.23
  race_white: 264229
  race_black: 64101
  race_asian: 7861
  race_native: 1084
  hispanic: 30267
  bachelors_plus: 136472
districts:
  - to: "us/states/tn/districts/03"
    rel: in-district
    area_weight: 0.997
  - to: "us/states/tn/districts/senate/11"
    rel: in-district
    area_weight: 0.7795
  - to: "us/states/tn/districts/senate/10"
    rel: in-district
    area_weight: 0.2203
  - to: "us/states/tn/districts/house/27"
    rel: in-district
    area_weight: 0.317
  - to: "us/states/tn/districts/house/29"
    rel: in-district
    area_weight: 0.2611
  - to: "us/states/tn/districts/house/26"
    rel: in-district
    area_weight: 0.2396
  - to: "us/states/tn/districts/house/30"
    rel: in-district
    area_weight: 0.0986
  - to: "us/states/tn/districts/house/28"
    rel: in-district
    area_weight: 0.0834
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, tn]
timestamp: "2026-07-03"
---

# Hamilton County, TN

County jurisdiction — 1 officeholders mapped.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 376192 |
| Under 18 | 79311 |
| 18–64 | 227795 |
| 65+ | 69086 |
| Median household income | 76183 |
| Poverty rate | 13.08 |
| Homeownership rate | 63.91 |
| Unemployment rate | 4.37 |
| Median home value | 312800 |
| Gini index | 0.485 |
| Vacancy rate | 8.23 |
| White | 264229 |
| Black | 64101 |
| Asian | 7861 |
| Native | 1084 |
| Hispanic/Latino | 30267 |
| Bachelor's or higher | 136472 |

## Districts

- [TN-03](/us/states/tn/districts/03.md) — 100% (congressional)
- [TN Senate District 11](/us/states/tn/districts/senate/11.md) — 78% (state senate)
- [TN Senate District 10](/us/states/tn/districts/senate/10.md) — 22% (state senate)
- [TN House District 27](/us/states/tn/districts/house/27.md) — 32% (state house)
- [TN House District 29](/us/states/tn/districts/house/29.md) — 26% (state house)
- [TN House District 26](/us/states/tn/districts/house/26.md) — 24% (state house)
- [TN House District 30](/us/states/tn/districts/house/30.md) — 10% (state house)
- [TN House District 28](/us/states/tn/districts/house/28.md) — 8% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
