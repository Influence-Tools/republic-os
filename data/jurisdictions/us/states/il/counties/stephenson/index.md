---
type: Jurisdiction
title: "Stephenson County, IL"
classification: county
fips: "17177"
state: "IL"
demographics:
  population: 43768
  population_under_18: 9296
  population_18_64: 23801
  population_65_plus: 10671
  median_household_income: 64043
  poverty_rate: 13.93
  homeownership_rate: 70.91
  unemployment_rate: 4.35
  median_home_value: 134900
  gini_index: 0.42
  vacancy_rate: 9.25
  race_white: 34830
  race_black: 3779
  race_asian: 361
  race_native: 170
  hispanic: 2457
  bachelors_plus: 8638
districts:
  - to: "us/states/il/districts/17"
    rel: in-district
    area_weight: 0.5384
  - to: "us/states/il/districts/16"
    rel: in-district
    area_weight: 0.4613
  - to: "us/states/il/districts/senate/45"
    rel: in-district
    area_weight: 0.9998
  - to: "us/states/il/districts/house/89"
    rel: in-district
    area_weight: 0.5443
  - to: "us/states/il/districts/house/90"
    rel: in-district
    area_weight: 0.4555
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, il]
timestamp: "2026-07-03"
---

# Stephenson County, IL

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 43768 |
| Under 18 | 9296 |
| 18–64 | 23801 |
| 65+ | 10671 |
| Median household income | 64043 |
| Poverty rate | 13.93 |
| Homeownership rate | 70.91 |
| Unemployment rate | 4.35 |
| Median home value | 134900 |
| Gini index | 0.42 |
| Vacancy rate | 9.25 |
| White | 34830 |
| Black | 3779 |
| Asian | 361 |
| Native | 170 |
| Hispanic/Latino | 2457 |
| Bachelor's or higher | 8638 |

## Districts

- [IL-17](/us/states/il/districts/17.md) — 54% (congressional)
- [IL-16](/us/states/il/districts/16.md) — 46% (congressional)
- [IL Senate District 45](/us/states/il/districts/senate/45.md) — 100% (state senate)
- [IL House District 89](/us/states/il/districts/house/89.md) — 54% (state house)
- [IL House District 90](/us/states/il/districts/house/90.md) — 46% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
