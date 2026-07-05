---
type: Jurisdiction
title: "Calhoun County, WV"
classification: county
fips: "54013"
state: "WV"
demographics:
  population: 6048
  population_under_18: 1147
  population_18_64: 3304
  population_65_plus: 1597
  median_household_income: 43980
  poverty_rate: 32.86
  homeownership_rate: 87.13
  unemployment_rate: 8.91
  median_home_value: 100500
  gini_index: 0.5689
  vacancy_rate: 20.72
  race_white: 5794
  race_black: 5
  race_asian: 3
  race_native: 9
  hispanic: 39
  bachelors_plus: 620
districts:
  - to: "us/states/wv/districts/01"
    rel: in-district
    area_weight: 0.9978
  - to: "us/states/wv/districts/senate/12"
    rel: in-district
    area_weight: 0.9995
  - to: "us/states/wv/districts/house/62"
    rel: in-district
    area_weight: 0.9995
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, wv]
timestamp: "2026-07-03"
---

# Calhoun County, WV

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 6048 |
| Under 18 | 1147 |
| 18–64 | 3304 |
| 65+ | 1597 |
| Median household income | 43980 |
| Poverty rate | 32.86 |
| Homeownership rate | 87.13 |
| Unemployment rate | 8.91 |
| Median home value | 100500 |
| Gini index | 0.5689 |
| Vacancy rate | 20.72 |
| White | 5794 |
| Black | 5 |
| Asian | 3 |
| Native | 9 |
| Hispanic/Latino | 39 |
| Bachelor's or higher | 620 |

## Districts

- [WV-01](/us/states/wv/districts/01.md) — 100% (congressional)
- [WV Senate District 12](/us/states/wv/districts/senate/12.md) — 100% (state senate)
- [WV House District 62](/us/states/wv/districts/house/62.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
