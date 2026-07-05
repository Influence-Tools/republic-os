---
type: Jurisdiction
title: "Summers County, WV"
classification: county
fips: "54089"
state: "WV"
demographics:
  population: 11729
  population_under_18: 1838
  population_18_64: 6709
  population_65_plus: 3182
  median_household_income: 40699
  poverty_rate: 23.79
  homeownership_rate: 81.15
  unemployment_rate: 2.2
  median_home_value: 140100
  gini_index: 0.4386
  vacancy_rate: 28.45
  race_white: 10651
  race_black: 718
  race_asian: 0
  race_native: 27
  hispanic: 157
  bachelors_plus: 2460
districts:
  - to: "us/states/wv/districts/01"
    rel: in-district
    area_weight: 1.0
  - to: "us/states/wv/districts/senate/10"
    rel: in-district
    area_weight: 0.9998
  - to: "us/states/wv/districts/house/41"
    rel: in-district
    area_weight: 0.6329
  - to: "us/states/wv/districts/house/40"
    rel: in-district
    area_weight: 0.367
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, wv]
timestamp: "2026-07-03"
---

# Summers County, WV

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 11729 |
| Under 18 | 1838 |
| 18–64 | 6709 |
| 65+ | 3182 |
| Median household income | 40699 |
| Poverty rate | 23.79 |
| Homeownership rate | 81.15 |
| Unemployment rate | 2.2 |
| Median home value | 140100 |
| Gini index | 0.4386 |
| Vacancy rate | 28.45 |
| White | 10651 |
| Black | 718 |
| Asian | 0 |
| Native | 27 |
| Hispanic/Latino | 157 |
| Bachelor's or higher | 2460 |

## Districts

- [WV-01](/us/states/wv/districts/01.md) — 100% (congressional)
- [WV Senate District 10](/us/states/wv/districts/senate/10.md) — 100% (state senate)
- [WV House District 41](/us/states/wv/districts/house/41.md) — 63% (state house)
- [WV House District 40](/us/states/wv/districts/house/40.md) — 37% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
