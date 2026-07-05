---
type: Jurisdiction
title: "Umatilla County, OR"
classification: county
fips: "41059"
state: "OR"
demographics:
  population: 79940
  population_under_18: 19651
  population_18_64: 47197
  population_65_plus: 13092
  median_household_income: 67728
  poverty_rate: 11.78
  homeownership_rate: 67.93
  unemployment_rate: 5.04
  median_home_value: 282600
  gini_index: 0.4232
  vacancy_rate: 10.85
  race_white: 53277
  race_black: 582
  race_asian: 560
  race_native: 2326
  hispanic: 23747
  bachelors_plus: 13182
districts:
  - to: "us/states/or/districts/02"
    rel: in-district
    area_weight: 0.9998
  - to: "us/states/or/districts/senate/29"
    rel: in-district
    area_weight: 0.9998
  - to: "us/states/or/districts/house/58"
    rel: in-district
    area_weight: 0.8338
  - to: "us/states/or/districts/house/57"
    rel: in-district
    area_weight: 0.166
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, or]
timestamp: "2026-07-03"
---

# Umatilla County, OR

County jurisdiction — 1 officeholders mapped.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 79940 |
| Under 18 | 19651 |
| 18–64 | 47197 |
| 65+ | 13092 |
| Median household income | 67728 |
| Poverty rate | 11.78 |
| Homeownership rate | 67.93 |
| Unemployment rate | 5.04 |
| Median home value | 282600 |
| Gini index | 0.4232 |
| Vacancy rate | 10.85 |
| White | 53277 |
| Black | 582 |
| Asian | 560 |
| Native | 2326 |
| Hispanic/Latino | 23747 |
| Bachelor's or higher | 13182 |

## Districts

- [OR-02](/us/states/or/districts/02.md) — 100% (congressional)
- [OR Senate District 29](/us/states/or/districts/senate/29.md) — 100% (state senate)
- [OR House District 58](/us/states/or/districts/house/58.md) — 83% (state house)
- [OR House District 57](/us/states/or/districts/house/57.md) — 17% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
