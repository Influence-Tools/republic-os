---
type: Jurisdiction
title: "Citrus County, FL"
classification: county
fips: "12017"
state: "FL"
demographics:
  population: 162472
  population_under_18: 26288
  population_18_64: 34468
  population_65_plus: 101716
  median_household_income: 56546
  poverty_rate: 15.59
  homeownership_rate: 85.23
  unemployment_rate: 6.35
  median_home_value: 245500
  gini_index: 0.4898
  vacancy_rate: 16.06
  race_white: 142299
  race_black: 2912
  race_asian: 2204
  race_native: 439
  hispanic: 11303
  bachelors_plus: 36543
districts:
  - to: "us/states/fl/districts/12"
    rel: in-district
    area_weight: 0.6814
  - to: "us/states/fl/districts/senate/11"
    rel: in-district
    area_weight: 0.6872
  - to: "us/states/fl/districts/house/23"
    rel: in-district
    area_weight: 0.6872
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, fl]
timestamp: "2026-07-03"
---

# Citrus County, FL

County jurisdiction — 28 officeholders mapped.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 162472 |
| Under 18 | 26288 |
| 18–64 | 34468 |
| 65+ | 101716 |
| Median household income | 56546 |
| Poverty rate | 15.59 |
| Homeownership rate | 85.23 |
| Unemployment rate | 6.35 |
| Median home value | 245500 |
| Gini index | 0.4898 |
| Vacancy rate | 16.06 |
| White | 142299 |
| Black | 2912 |
| Asian | 2204 |
| Native | 439 |
| Hispanic/Latino | 11303 |
| Bachelor's or higher | 36543 |

## Districts

- [FL-12](/us/states/fl/districts/12.md) — 68% (congressional)
- [FL Senate District 11](/us/states/fl/districts/senate/11.md) — 69% (state senate)
- [FL House District 23](/us/states/fl/districts/house/23.md) — 69% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
