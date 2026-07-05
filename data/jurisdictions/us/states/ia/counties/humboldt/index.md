---
type: Jurisdiction
title: "Humboldt County, IA"
classification: county
fips: "19091"
state: "IA"
demographics:
  population: 9591
  population_under_18: 2274
  population_18_64: 5242
  population_65_plus: 2075
  median_household_income: 71946
  poverty_rate: 12.87
  homeownership_rate: 77.15
  unemployment_rate: 5.04
  median_home_value: 155800
  gini_index: 0.4592
  vacancy_rate: 8.34
  race_white: 8738
  race_black: 32
  race_asian: 98
  race_native: 16
  hispanic: 551
  bachelors_plus: 1593
districts:
  - to: "us/states/ia/districts/04"
    rel: in-district
    area_weight: 1.0
  - to: "us/states/ia/districts/senate/28"
    rel: in-district
    area_weight: 0.9999
  - to: "us/states/ia/districts/house/56"
    rel: in-district
    area_weight: 0.9999
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, ia]
timestamp: "2026-07-03"
---

# Humboldt County, IA

County jurisdiction — 1 officeholders mapped.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 9591 |
| Under 18 | 2274 |
| 18–64 | 5242 |
| 65+ | 2075 |
| Median household income | 71946 |
| Poverty rate | 12.87 |
| Homeownership rate | 77.15 |
| Unemployment rate | 5.04 |
| Median home value | 155800 |
| Gini index | 0.4592 |
| Vacancy rate | 8.34 |
| White | 8738 |
| Black | 32 |
| Asian | 98 |
| Native | 16 |
| Hispanic/Latino | 551 |
| Bachelor's or higher | 1593 |

## Districts

- [IA-04](/us/states/ia/districts/04.md) — 100% (congressional)
- [IA Senate District 28](/us/states/ia/districts/senate/28.md) — 100% (state senate)
- [IA House District 56](/us/states/ia/districts/house/56.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
