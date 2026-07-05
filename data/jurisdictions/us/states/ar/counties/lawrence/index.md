---
type: Jurisdiction
title: "Lawrence County, AR"
classification: county
fips: "05075"
state: "AR"
demographics:
  population: 16238
  population_under_18: 3624
  population_18_64: 9537
  population_65_plus: 3077
  median_household_income: 44882
  poverty_rate: 20.1
  homeownership_rate: 66.55
  unemployment_rate: 5.79
  median_home_value: 98900
  gini_index: 0.4719
  vacancy_rate: 13.49
  race_white: 14969
  race_black: 151
  race_asian: 14
  race_native: 9
  hispanic: 362
  bachelors_plus: 2114
districts:
  - to: "us/states/ar/districts/01"
    rel: in-district
    area_weight: 1.0
  - to: "us/states/ar/districts/senate/22"
    rel: in-district
    area_weight: 0.7762
  - to: "us/states/ar/districts/senate/21"
    rel: in-district
    area_weight: 0.2237
  - to: "us/states/ar/districts/house/28"
    rel: in-district
    area_weight: 0.7763
  - to: "us/states/ar/districts/house/30"
    rel: in-district
    area_weight: 0.2235
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, ar]
timestamp: "2026-07-03"
---

# Lawrence County, AR

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 16238 |
| Under 18 | 3624 |
| 18–64 | 9537 |
| 65+ | 3077 |
| Median household income | 44882 |
| Poverty rate | 20.1 |
| Homeownership rate | 66.55 |
| Unemployment rate | 5.79 |
| Median home value | 98900 |
| Gini index | 0.4719 |
| Vacancy rate | 13.49 |
| White | 14969 |
| Black | 151 |
| Asian | 14 |
| Native | 9 |
| Hispanic/Latino | 362 |
| Bachelor's or higher | 2114 |

## Districts

- [AR-01](/us/states/ar/districts/01.md) — 100% (congressional)
- [AR Senate District 22](/us/states/ar/districts/senate/22.md) — 78% (state senate)
- [AR Senate District 21](/us/states/ar/districts/senate/21.md) — 22% (state senate)
- [AR House District 28](/us/states/ar/districts/house/28.md) — 78% (state house)
- [AR House District 30](/us/states/ar/districts/house/30.md) — 22% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
