---
type: Jurisdiction
title: "Iberville Parish, LA"
classification: county
fips: "22047"
state: "LA"
demographics:
  population: 29815
  population_under_18: 5971
  population_18_64: 18617
  population_65_plus: 5227
  median_household_income: 54000
  poverty_rate: 19.91
  homeownership_rate: 75.11
  unemployment_rate: 6.13
  median_home_value: 172800
  gini_index: 0.4741
  vacancy_rate: 16.6
  race_white: 13957
  race_black: 12902
  race_asian: 6
  race_native: 64
  hispanic: 1546
  bachelors_plus: 5427
districts:
  - to: "us/states/la/districts/02"
    rel: in-district
    area_weight: 0.9939
  - to: "us/states/la/districts/senate/17"
    rel: in-district
    area_weight: 0.7861
  - to: "us/states/la/districts/senate/2"
    rel: in-district
    area_weight: 0.2136
  - to: "us/states/la/districts/house/60"
    rel: in-district
    area_weight: 0.7818
  - to: "us/states/la/districts/house/18"
    rel: in-district
    area_weight: 0.2179
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, la]
timestamp: "2026-07-03"
---

# Iberville Parish, LA

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 29815 |
| Under 18 | 5971 |
| 18–64 | 18617 |
| 65+ | 5227 |
| Median household income | 54000 |
| Poverty rate | 19.91 |
| Homeownership rate | 75.11 |
| Unemployment rate | 6.13 |
| Median home value | 172800 |
| Gini index | 0.4741 |
| Vacancy rate | 16.6 |
| White | 13957 |
| Black | 12902 |
| Asian | 6 |
| Native | 64 |
| Hispanic/Latino | 1546 |
| Bachelor's or higher | 5427 |

## Districts

- [LA-02](/us/states/la/districts/02.md) — 99% (congressional)
- [LA Senate District 17](/us/states/la/districts/senate/17.md) — 79% (state senate)
- [LA Senate District 2](/us/states/la/districts/senate/2.md) — 21% (state senate)
- [LA House District 60](/us/states/la/districts/house/60.md) — 78% (state house)
- [LA House District 18](/us/states/la/districts/house/18.md) — 22% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
