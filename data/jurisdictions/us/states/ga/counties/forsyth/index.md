---
type: Jurisdiction
title: "Forsyth County, GA"
classification: county
fips: "13117"
state: "GA"
demographics:
  population: 267287
  population_under_18: 68772
  population_18_64: 164559
  population_65_plus: 33956
  median_household_income: 143784
  poverty_rate: 4.34
  homeownership_rate: 84.43
  unemployment_rate: 3.51
  median_home_value: 550400
  gini_index: 0.3919
  vacancy_rate: 3.83
  race_white: 169658
  race_black: 11421
  race_asian: 52530
  race_native: 806
  hispanic: 27069
  bachelors_plus: 140806
districts:
  - to: "us/states/ga/districts/07"
    rel: in-district
    area_weight: 0.9993
  - to: "us/states/ga/districts/senate/27"
    rel: in-district
    area_weight: 0.877
  - to: "us/states/ga/districts/senate/48"
    rel: in-district
    area_weight: 0.1227
  - to: "us/states/ga/districts/house/28"
    rel: in-district
    area_weight: 0.3127
  - to: "us/states/ga/districts/house/26"
    rel: in-district
    area_weight: 0.2443
  - to: "us/states/ga/districts/house/24"
    rel: in-district
    area_weight: 0.1661
  - to: "us/states/ga/districts/house/11"
    rel: in-district
    area_weight: 0.1527
  - to: "us/states/ga/districts/house/25"
    rel: in-district
    area_weight: 0.0974
  - to: "us/states/ga/districts/house/100"
    rel: in-district
    area_weight: 0.0265
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, ga]
timestamp: "2026-07-03"
---

# Forsyth County, GA

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 267287 |
| Under 18 | 68772 |
| 18–64 | 164559 |
| 65+ | 33956 |
| Median household income | 143784 |
| Poverty rate | 4.34 |
| Homeownership rate | 84.43 |
| Unemployment rate | 3.51 |
| Median home value | 550400 |
| Gini index | 0.3919 |
| Vacancy rate | 3.83 |
| White | 169658 |
| Black | 11421 |
| Asian | 52530 |
| Native | 806 |
| Hispanic/Latino | 27069 |
| Bachelor's or higher | 140806 |

## Districts

- [GA-07](/us/states/ga/districts/07.md) — 100% (congressional)
- [GA Senate District 27](/us/states/ga/districts/senate/27.md) — 88% (state senate)
- [GA Senate District 48](/us/states/ga/districts/senate/48.md) — 12% (state senate)
- [GA House District 28](/us/states/ga/districts/house/28.md) — 31% (state house)
- [GA House District 26](/us/states/ga/districts/house/26.md) — 24% (state house)
- [GA House District 24](/us/states/ga/districts/house/24.md) — 17% (state house)
- [GA House District 11](/us/states/ga/districts/house/11.md) — 15% (state house)
- [GA House District 25](/us/states/ga/districts/house/25.md) — 10% (state house)
- [GA House District 100](/us/states/ga/districts/house/100.md) — 3% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
