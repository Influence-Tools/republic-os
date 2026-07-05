---
type: Jurisdiction
title: "Jefferson County, WA"
classification: county
fips: "53031"
state: "WA"
demographics:
  population: 33577
  population_under_18: 3747
  population_18_64: 16157
  population_65_plus: 13673
  median_household_income: 74048
  poverty_rate: 11.09
  homeownership_rate: 79.05
  unemployment_rate: 6.65
  median_home_value: 535000
  gini_index: 0.487
  vacancy_rate: 16.35
  race_white: 28727
  race_black: 131
  race_asian: 434
  race_native: 357
  hispanic: 1480
  bachelors_plus: 18142
districts:
  - to: "us/states/wa/districts/06"
    rel: in-district
    area_weight: 0.8358
  - to: "us/states/wa/districts/senate/24"
    rel: in-district
    area_weight: 0.8341
  - to: "us/states/wa/districts/house/24"
    rel: in-district
    area_weight: 0.8341
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, wa]
timestamp: "2026-07-03"
---

# Jefferson County, WA

County jurisdiction — 1 officeholders mapped.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 33577 |
| Under 18 | 3747 |
| 18–64 | 16157 |
| 65+ | 13673 |
| Median household income | 74048 |
| Poverty rate | 11.09 |
| Homeownership rate | 79.05 |
| Unemployment rate | 6.65 |
| Median home value | 535000 |
| Gini index | 0.487 |
| Vacancy rate | 16.35 |
| White | 28727 |
| Black | 131 |
| Asian | 434 |
| Native | 357 |
| Hispanic/Latino | 1480 |
| Bachelor's or higher | 18142 |

## Districts

- [WA-06](/us/states/wa/districts/06.md) — 84% (congressional)
- [WA Senate District 24](/us/states/wa/districts/senate/24.md) — 83% (state senate)
- [WA House District 24](/us/states/wa/districts/house/24.md) — 83% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
