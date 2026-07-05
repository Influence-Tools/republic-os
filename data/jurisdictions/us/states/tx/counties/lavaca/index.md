---
type: Jurisdiction
title: "Lavaca County, TX"
classification: county
fips: "48285"
state: "TX"
demographics:
  population: 20552
  population_under_18: 4826
  population_18_64: 10776
  population_65_plus: 4950
  median_household_income: 63240
  poverty_rate: 11.45
  homeownership_rate: 78.34
  unemployment_rate: 3.05
  median_home_value: 228300
  gini_index: 0.4358
  vacancy_rate: 19.41
  race_white: 15211
  race_black: 749
  race_asian: 71
  race_native: 16
  hispanic: 4129
  bachelors_plus: 4138
districts:
  - to: "us/states/tx/districts/27"
    rel: in-district
    area_weight: 0.9998
  - to: "us/states/tx/districts/senate/18"
    rel: in-district
    area_weight: 0.9998
  - to: "us/states/tx/districts/house/30"
    rel: in-district
    area_weight: 0.9998
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, tx]
timestamp: "2026-07-03"
---

# Lavaca County, TX

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 20552 |
| Under 18 | 4826 |
| 18–64 | 10776 |
| 65+ | 4950 |
| Median household income | 63240 |
| Poverty rate | 11.45 |
| Homeownership rate | 78.34 |
| Unemployment rate | 3.05 |
| Median home value | 228300 |
| Gini index | 0.4358 |
| Vacancy rate | 19.41 |
| White | 15211 |
| Black | 749 |
| Asian | 71 |
| Native | 16 |
| Hispanic/Latino | 4129 |
| Bachelor's or higher | 4138 |

## Districts

- [TX-27](/us/states/tx/districts/27.md) — 100% (congressional)
- [TX Senate District 18](/us/states/tx/districts/senate/18.md) — 100% (state senate)
- [TX House District 30](/us/states/tx/districts/house/30.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
