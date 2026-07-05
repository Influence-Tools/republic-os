---
type: Jurisdiction
title: "Mohave County, AZ"
classification: county
fips: "04015"
state: "AZ"
demographics:
  population: 220517
  population_under_18: 35598
  population_18_64: 112983
  population_65_plus: 71936
  median_household_income: 57684
  poverty_rate: 16.09
  homeownership_rate: 74.07
  unemployment_rate: 7.25
  median_home_value: 281000
  gini_index: 0.4702
  vacancy_rate: 16.33
  race_white: 175733
  race_black: 2377
  race_asian: 2554
  race_native: 3771
  hispanic: 37708
  bachelors_plus: 36183
districts:
  - to: "us/states/az/districts/09"
    rel: in-district
    area_weight: 0.9292
  - to: "us/states/az/districts/02"
    rel: in-district
    area_weight: 0.0705
  - to: "us/states/az/districts/senate/30"
    rel: in-district
    area_weight: 0.9294
  - to: "us/states/az/districts/senate/6"
    rel: in-district
    area_weight: 0.0704
  - to: "us/states/az/districts/house/30"
    rel: in-district
    area_weight: 0.9294
  - to: "us/states/az/districts/house/6"
    rel: in-district
    area_weight: 0.0704
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, az]
timestamp: "2026-07-03"
---

# Mohave County, AZ

County jurisdiction — 1 officeholders mapped.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 220517 |
| Under 18 | 35598 |
| 18–64 | 112983 |
| 65+ | 71936 |
| Median household income | 57684 |
| Poverty rate | 16.09 |
| Homeownership rate | 74.07 |
| Unemployment rate | 7.25 |
| Median home value | 281000 |
| Gini index | 0.4702 |
| Vacancy rate | 16.33 |
| White | 175733 |
| Black | 2377 |
| Asian | 2554 |
| Native | 3771 |
| Hispanic/Latino | 37708 |
| Bachelor's or higher | 36183 |

## Districts

- [AZ-09](/us/states/az/districts/09.md) — 93% (congressional)
- [AZ-02](/us/states/az/districts/02.md) — 7% (congressional)
- [AZ Senate District 30](/us/states/az/districts/senate/30.md) — 93% (state senate)
- [AZ Senate District 6](/us/states/az/districts/senate/6.md) — 7% (state senate)
- [AZ House District 30](/us/states/az/districts/house/30.md) — 93% (state house)
- [AZ House District 6](/us/states/az/districts/house/6.md) — 7% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
