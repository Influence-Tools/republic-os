---
type: Jurisdiction
title: "Waushara County, WI"
classification: county
fips: "55137"
state: "WI"
demographics:
  population: 24868
  population_under_18: 4409
  population_18_64: 13947
  population_65_plus: 6512
  median_household_income: 67107
  poverty_rate: 10.92
  homeownership_rate: 84.18
  unemployment_rate: 3.91
  median_home_value: 203100
  gini_index: 0.4344
  vacancy_rate: 28.83
  race_white: 22058
  race_black: 450
  race_asian: 111
  race_native: 160
  hispanic: 1740
  bachelors_plus: 4423
districts:
  - to: "us/states/wi/districts/06"
    rel: in-district
    area_weight: 0.9999
  - to: "us/states/wi/districts/senate/19"
    rel: in-district
    area_weight: 0.9986
  - to: "us/states/wi/districts/house/57"
    rel: in-district
    area_weight: 0.9986
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, wi]
timestamp: "2026-07-03"
---

# Waushara County, WI

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 24868 |
| Under 18 | 4409 |
| 18–64 | 13947 |
| 65+ | 6512 |
| Median household income | 67107 |
| Poverty rate | 10.92 |
| Homeownership rate | 84.18 |
| Unemployment rate | 3.91 |
| Median home value | 203100 |
| Gini index | 0.4344 |
| Vacancy rate | 28.83 |
| White | 22058 |
| Black | 450 |
| Asian | 111 |
| Native | 160 |
| Hispanic/Latino | 1740 |
| Bachelor's or higher | 4423 |

## Districts

- [WI-06](/us/states/wi/districts/06.md) — 100% (congressional)
- [WI Senate District 19](/us/states/wi/districts/senate/19.md) — 100% (state senate)
- [WI House District 57](/us/states/wi/districts/house/57.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
