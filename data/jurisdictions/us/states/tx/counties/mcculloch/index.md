---
type: Jurisdiction
title: "McCulloch County, TX"
classification: county
fips: "48307"
state: "TX"
demographics:
  population: 7514
  population_under_18: 1647
  population_18_64: 4089
  population_65_plus: 1778
  median_household_income: 54043
  poverty_rate: 15.33
  homeownership_rate: 66.58
  unemployment_rate: 9.04
  median_home_value: 150500
  gini_index: 0.4656
  vacancy_rate: 21.85
  race_white: 5186
  race_black: 71
  race_asian: 10
  race_native: 36
  hispanic: 2289
  bachelors_plus: 1748
districts:
  - to: "us/states/tx/districts/11"
    rel: in-district
    area_weight: 1.0
  - to: "us/states/tx/districts/senate/28"
    rel: in-district
    area_weight: 1.0
  - to: "us/states/tx/districts/house/53"
    rel: in-district
    area_weight: 0.9999
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, tx]
timestamp: "2026-07-03"
---

# McCulloch County, TX

County jurisdiction — 1 officeholders mapped.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 7514 |
| Under 18 | 1647 |
| 18–64 | 4089 |
| 65+ | 1778 |
| Median household income | 54043 |
| Poverty rate | 15.33 |
| Homeownership rate | 66.58 |
| Unemployment rate | 9.04 |
| Median home value | 150500 |
| Gini index | 0.4656 |
| Vacancy rate | 21.85 |
| White | 5186 |
| Black | 71 |
| Asian | 10 |
| Native | 36 |
| Hispanic/Latino | 2289 |
| Bachelor's or higher | 1748 |

## Districts

- [TX-11](/us/states/tx/districts/11.md) — 100% (congressional)
- [TX Senate District 28](/us/states/tx/districts/senate/28.md) — 100% (state senate)
- [TX House District 53](/us/states/tx/districts/house/53.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
