---
type: Jurisdiction
title: "Gordon County, GA"
classification: county
fips: "13129"
state: "GA"
demographics:
  population: 59100
  population_under_18: 13672
  population_18_64: 36066
  population_65_plus: 9362
  median_household_income: 63650
  poverty_rate: 11.96
  homeownership_rate: 73.9
  unemployment_rate: 3.66
  median_home_value: 222900
  gini_index: 0.442
  vacancy_rate: 9.4
  race_white: 46004
  race_black: 2186
  race_asian: 632
  race_native: 758
  hispanic: 9657
  bachelors_plus: 10878
districts:
  - to: "us/states/ga/districts/11"
    rel: in-district
    area_weight: 0.9928
  - to: "us/states/ga/districts/14"
    rel: in-district
    area_weight: 0.0072
  - to: "us/states/ga/districts/senate/54"
    rel: in-district
    area_weight: 0.7427
  - to: "us/states/ga/districts/senate/52"
    rel: in-district
    area_weight: 0.2572
  - to: "us/states/ga/districts/house/5"
    rel: in-district
    area_weight: 0.8211
  - to: "us/states/ga/districts/house/6"
    rel: in-district
    area_weight: 0.1787
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, ga]
timestamp: "2026-07-03"
---

# Gordon County, GA

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 59100 |
| Under 18 | 13672 |
| 18–64 | 36066 |
| 65+ | 9362 |
| Median household income | 63650 |
| Poverty rate | 11.96 |
| Homeownership rate | 73.9 |
| Unemployment rate | 3.66 |
| Median home value | 222900 |
| Gini index | 0.442 |
| Vacancy rate | 9.4 |
| White | 46004 |
| Black | 2186 |
| Asian | 632 |
| Native | 758 |
| Hispanic/Latino | 9657 |
| Bachelor's or higher | 10878 |

## Districts

- [GA-11](/us/states/ga/districts/11.md) — 99% (congressional)
- [GA-14](/us/states/ga/districts/14.md) — 1% (congressional)
- [GA Senate District 54](/us/states/ga/districts/senate/54.md) — 74% (state senate)
- [GA Senate District 52](/us/states/ga/districts/senate/52.md) — 26% (state senate)
- [GA House District 5](/us/states/ga/districts/house/5.md) — 82% (state house)
- [GA House District 6](/us/states/ga/districts/house/6.md) — 18% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
