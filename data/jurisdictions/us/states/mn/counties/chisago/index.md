---
type: Jurisdiction
title: "Chisago County, MN"
classification: county
fips: "27025"
state: "MN"
demographics:
  population: 57991
  population_under_18: 12958
  population_18_64: 35123
  population_65_plus: 9910
  median_household_income: 99400
  poverty_rate: 5.95
  homeownership_rate: 85.92
  unemployment_rate: 4.09
  median_home_value: 351900
  gini_index: 0.3884
  vacancy_rate: 7.1
  race_white: 52595
  race_black: 728
  race_asian: 1157
  race_native: 235
  hispanic: 1644
  bachelors_plus: 12971
districts:
  - to: "us/states/mn/districts/08"
    rel: in-district
    area_weight: 0.9996
  - to: "us/states/mn/districts/senate/28"
    rel: in-district
    area_weight: 0.8242
  - to: "us/states/mn/districts/senate/11"
    rel: in-district
    area_weight: 0.1755
  - to: "us/states/mn/districts/house/28b"
    rel: in-district
    area_weight: 0.6722
  - to: "us/states/mn/districts/house/11b"
    rel: in-district
    area_weight: 0.1755
  - to: "us/states/mn/districts/house/28a"
    rel: in-district
    area_weight: 0.1519
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, mn]
timestamp: "2026-07-03"
---

# Chisago County, MN

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 57991 |
| Under 18 | 12958 |
| 18–64 | 35123 |
| 65+ | 9910 |
| Median household income | 99400 |
| Poverty rate | 5.95 |
| Homeownership rate | 85.92 |
| Unemployment rate | 4.09 |
| Median home value | 351900 |
| Gini index | 0.3884 |
| Vacancy rate | 7.1 |
| White | 52595 |
| Black | 728 |
| Asian | 1157 |
| Native | 235 |
| Hispanic/Latino | 1644 |
| Bachelor's or higher | 12971 |

## Districts

- [MN-08](/us/states/mn/districts/08.md) — 100% (congressional)
- [MN Senate District 28](/us/states/mn/districts/senate/28.md) — 82% (state senate)
- [MN Senate District 11](/us/states/mn/districts/senate/11.md) — 18% (state senate)
- [MN House District 28B](/us/states/mn/districts/house/28b.md) — 67% (state house)
- [MN House District 11B](/us/states/mn/districts/house/11b.md) — 18% (state house)
- [MN House District 28A](/us/states/mn/districts/house/28a.md) — 15% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
