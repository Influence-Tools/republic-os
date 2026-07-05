---
type: Jurisdiction
title: "Monroe County, MI"
classification: county
fips: "26115"
state: "MI"
demographics:
  population: 155505
  population_under_18: 32522
  population_18_64: 92053
  population_65_plus: 30930
  median_household_income: 77335
  poverty_rate: 10.53
  homeownership_rate: 81.71
  unemployment_rate: 5.13
  median_home_value: 228900
  gini_index: 0.4232
  vacancy_rate: 5.35
  race_white: 139931
  race_black: 3386
  race_asian: 623
  race_native: 165
  hispanic: 6830
  bachelors_plus: 35326
districts:
  - to: "us/states/mi/districts/05"
    rel: in-district
    area_weight: 0.8253
  - to: "us/states/mi/districts/senate/16"
    rel: in-district
    area_weight: 0.8191
  - to: "us/states/mi/districts/house/30"
    rel: in-district
    area_weight: 0.3604
  - to: "us/states/mi/districts/house/31"
    rel: in-district
    area_weight: 0.3035
  - to: "us/states/mi/districts/house/29"
    rel: in-district
    area_weight: 0.0816
  - to: "us/states/mi/districts/house/28"
    rel: in-district
    area_weight: 0.0773
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, mi]
timestamp: "2026-07-03"
---

# Monroe County, MI

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 155505 |
| Under 18 | 32522 |
| 18–64 | 92053 |
| 65+ | 30930 |
| Median household income | 77335 |
| Poverty rate | 10.53 |
| Homeownership rate | 81.71 |
| Unemployment rate | 5.13 |
| Median home value | 228900 |
| Gini index | 0.4232 |
| Vacancy rate | 5.35 |
| White | 139931 |
| Black | 3386 |
| Asian | 623 |
| Native | 165 |
| Hispanic/Latino | 6830 |
| Bachelor's or higher | 35326 |

## Districts

- [MI-05](/us/states/mi/districts/05.md) — 83% (congressional)
- [MI Senate District 16](/us/states/mi/districts/senate/16.md) — 82% (state senate)
- [MI House District 30](/us/states/mi/districts/house/30.md) — 36% (state house)
- [MI House District 31](/us/states/mi/districts/house/31.md) — 30% (state house)
- [MI House District 29](/us/states/mi/districts/house/29.md) — 8% (state house)
- [MI House District 28](/us/states/mi/districts/house/28.md) — 8% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
