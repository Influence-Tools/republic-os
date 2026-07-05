---
type: Jurisdiction
title: "Volusia County, FL"
classification: county
fips: "12127"
state: "FL"
demographics:
  population: 579622
  population_under_18: 100824
  population_18_64: 331664
  population_65_plus: 147134
  median_household_income: 70044
  poverty_rate: 11.76
  homeownership_rate: 73.71
  unemployment_rate: 4.13
  median_home_value: 313000
  gini_index: 0.4491
  vacancy_rate: 14.26
  race_white: 410175
  race_black: 61378
  race_asian: 11546
  race_native: 1529
  hispanic: 94499
  bachelors_plus: 165802
districts:
  - to: "us/states/fl/districts/06"
    rel: in-district
    area_weight: 0.4689
  - to: "us/states/fl/districts/07"
    rel: in-district
    area_weight: 0.4146
  - to: "us/states/fl/districts/senate/8"
    rel: in-district
    area_weight: 0.6965
  - to: "us/states/fl/districts/senate/7"
    rel: in-district
    area_weight: 0.1872
  - to: "us/states/fl/districts/house/30"
    rel: in-district
    area_weight: 0.2556
  - to: "us/states/fl/districts/house/27"
    rel: in-district
    area_weight: 0.2473
  - to: "us/states/fl/districts/house/29"
    rel: in-district
    area_weight: 0.2173
  - to: "us/states/fl/districts/house/28"
    rel: in-district
    area_weight: 0.1636
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, fl]
timestamp: "2026-07-03"
---

# Volusia County, FL

County jurisdiction — 100 officeholders mapped.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 579622 |
| Under 18 | 100824 |
| 18–64 | 331664 |
| 65+ | 147134 |
| Median household income | 70044 |
| Poverty rate | 11.76 |
| Homeownership rate | 73.71 |
| Unemployment rate | 4.13 |
| Median home value | 313000 |
| Gini index | 0.4491 |
| Vacancy rate | 14.26 |
| White | 410175 |
| Black | 61378 |
| Asian | 11546 |
| Native | 1529 |
| Hispanic/Latino | 94499 |
| Bachelor's or higher | 165802 |

## Districts

- [FL-06](/us/states/fl/districts/06.md) — 47% (congressional)
- [FL-07](/us/states/fl/districts/07.md) — 41% (congressional)
- [FL Senate District 8](/us/states/fl/districts/senate/8.md) — 70% (state senate)
- [FL Senate District 7](/us/states/fl/districts/senate/7.md) — 19% (state senate)
- [FL House District 30](/us/states/fl/districts/house/30.md) — 26% (state house)
- [FL House District 27](/us/states/fl/districts/house/27.md) — 25% (state house)
- [FL House District 29](/us/states/fl/districts/house/29.md) — 22% (state house)
- [FL House District 28](/us/states/fl/districts/house/28.md) — 16% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
