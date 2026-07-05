---
type: Jurisdiction
title: "Habersham County, GA"
classification: county
fips: "13137"
state: "GA"
demographics:
  population: 47793
  population_under_18: 10428
  population_18_64: 28119
  population_65_plus: 9246
  median_household_income: 67309
  poverty_rate: 14.08
  homeownership_rate: 72.8
  unemployment_rate: 2.7
  median_home_value: 238300
  gini_index: 0.4517
  vacancy_rate: 12.15
  race_white: 37564
  race_black: 1542
  race_asian: 1162
  race_native: 286
  hispanic: 7681
  bachelors_plus: 11405
districts:
  - to: "us/states/ga/districts/09"
    rel: in-district
    area_weight: 0.9997
  - to: "us/states/ga/districts/senate/50"
    rel: in-district
    area_weight: 1.0
  - to: "us/states/ga/districts/house/10"
    rel: in-district
    area_weight: 0.9223
  - to: "us/states/ga/districts/house/32"
    rel: in-district
    area_weight: 0.0773
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, ga]
timestamp: "2026-07-03"
---

# Habersham County, GA

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 47793 |
| Under 18 | 10428 |
| 18–64 | 28119 |
| 65+ | 9246 |
| Median household income | 67309 |
| Poverty rate | 14.08 |
| Homeownership rate | 72.8 |
| Unemployment rate | 2.7 |
| Median home value | 238300 |
| Gini index | 0.4517 |
| Vacancy rate | 12.15 |
| White | 37564 |
| Black | 1542 |
| Asian | 1162 |
| Native | 286 |
| Hispanic/Latino | 7681 |
| Bachelor's or higher | 11405 |

## Districts

- [GA-09](/us/states/ga/districts/09.md) — 100% (congressional)
- [GA Senate District 50](/us/states/ga/districts/senate/50.md) — 100% (state senate)
- [GA House District 10](/us/states/ga/districts/house/10.md) — 92% (state house)
- [GA House District 32](/us/states/ga/districts/house/32.md) — 8% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
