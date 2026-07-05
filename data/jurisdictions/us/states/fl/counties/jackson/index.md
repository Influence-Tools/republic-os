---
type: Jurisdiction
title: "Jackson County, FL"
classification: county
fips: "12063"
state: "FL"
demographics:
  population: 48250
  population_under_18: 9135
  population_18_64: 29037
  population_65_plus: 10078
  median_household_income: 49149
  poverty_rate: 19.46
  homeownership_rate: 75.93
  unemployment_rate: 4.52
  median_home_value: 120800
  gini_index: 0.4277
  vacancy_rate: 14.24
  race_white: 31631
  race_black: 12190
  race_asian: 276
  race_native: 148
  hispanic: 2598
  bachelors_plus: 7501
districts:
  - to: "us/states/fl/districts/02"
    rel: in-district
    area_weight: 0.9996
  - to: "us/states/fl/districts/senate/2"
    rel: in-district
    area_weight: 0.9999
  - to: "us/states/fl/districts/house/5"
    rel: in-district
    area_weight: 0.9999
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, fl]
timestamp: "2026-07-03"
---

# Jackson County, FL

County jurisdiction — 66 officeholders mapped.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 48250 |
| Under 18 | 9135 |
| 18–64 | 29037 |
| 65+ | 10078 |
| Median household income | 49149 |
| Poverty rate | 19.46 |
| Homeownership rate | 75.93 |
| Unemployment rate | 4.52 |
| Median home value | 120800 |
| Gini index | 0.4277 |
| Vacancy rate | 14.24 |
| White | 31631 |
| Black | 12190 |
| Asian | 276 |
| Native | 148 |
| Hispanic/Latino | 2598 |
| Bachelor's or higher | 7501 |

## Districts

- [FL-02](/us/states/fl/districts/02.md) — 100% (congressional)
- [FL Senate District 2](/us/states/fl/districts/senate/2.md) — 100% (state senate)
- [FL House District 5](/us/states/fl/districts/house/5.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
