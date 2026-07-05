---
type: Jurisdiction
title: "Highlands County, FL"
classification: county
fips: "12055"
state: "FL"
demographics:
  population: 105702
  population_under_18: 19267
  population_18_64: 24207
  population_65_plus: 62228
  median_household_income: 54897
  poverty_rate: 15.26
  homeownership_rate: 78.6
  unemployment_rate: 6.36
  median_home_value: 187900
  gini_index: 0.4567
  vacancy_rate: 20.05
  race_white: 72316
  race_black: 10359
  race_asian: 1598
  race_native: 751
  hispanic: 23465
  bachelors_plus: 22957
districts:
  - to: "us/states/fl/districts/18"
    rel: in-district
    area_weight: 1.0
  - to: "us/states/fl/districts/senate/29"
    rel: in-district
    area_weight: 0.9996
  - to: "us/states/fl/districts/house/83"
    rel: in-district
    area_weight: 0.9996
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, fl]
timestamp: "2026-07-03"
---

# Highlands County, FL

County jurisdiction — 31 officeholders mapped.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 105702 |
| Under 18 | 19267 |
| 18–64 | 24207 |
| 65+ | 62228 |
| Median household income | 54897 |
| Poverty rate | 15.26 |
| Homeownership rate | 78.6 |
| Unemployment rate | 6.36 |
| Median home value | 187900 |
| Gini index | 0.4567 |
| Vacancy rate | 20.05 |
| White | 72316 |
| Black | 10359 |
| Asian | 1598 |
| Native | 751 |
| Hispanic/Latino | 23465 |
| Bachelor's or higher | 22957 |

## Districts

- [FL-18](/us/states/fl/districts/18.md) — 100% (congressional)
- [FL Senate District 29](/us/states/fl/districts/senate/29.md) — 100% (state senate)
- [FL House District 83](/us/states/fl/districts/house/83.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
