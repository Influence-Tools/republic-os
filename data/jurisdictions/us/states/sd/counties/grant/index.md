---
type: Jurisdiction
title: "Grant County, SD"
classification: county
fips: "46051"
state: "SD"
demographics:
  population: 7563
  population_under_18: 1677
  population_18_64: 4119
  population_65_plus: 1767
  median_household_income: 75028
  poverty_rate: 11.58
  homeownership_rate: 75.64
  unemployment_rate: 2.74
  median_home_value: 171000
  gini_index: 0.4237
  vacancy_rate: 12.36
  race_white: 6862
  race_black: 28
  race_asian: 60
  race_native: 203
  hispanic: 559
  bachelors_plus: 1718
districts:
  - to: "us/states/sd/districts/00"
    rel: in-district
    area_weight: 0.9999
  - to: "us/states/sd/districts/senate/4"
    rel: in-district
    area_weight: 0.9999
  - to: "us/states/sd/districts/house/4"
    rel: in-district
    area_weight: 0.9999
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, sd]
timestamp: "2026-07-03"
---

# Grant County, SD

County jurisdiction — 1 officeholders mapped.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 7563 |
| Under 18 | 1677 |
| 18–64 | 4119 |
| 65+ | 1767 |
| Median household income | 75028 |
| Poverty rate | 11.58 |
| Homeownership rate | 75.64 |
| Unemployment rate | 2.74 |
| Median home value | 171000 |
| Gini index | 0.4237 |
| Vacancy rate | 12.36 |
| White | 6862 |
| Black | 28 |
| Asian | 60 |
| Native | 203 |
| Hispanic/Latino | 559 |
| Bachelor's or higher | 1718 |

## Districts

- [SD-00](/us/states/sd/districts/00.md) — 100% (congressional)
- [SD Senate District 4](/us/states/sd/districts/senate/4.md) — 100% (state senate)
- [SD House District 4](/us/states/sd/districts/house/4.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
