---
type: Jurisdiction
title: "Curry County, NM"
classification: county
fips: "35009"
state: "NM"
demographics:
  population: 47638
  population_under_18: 12637
  population_18_64: 28816
  population_65_plus: 6185
  median_household_income: 57309
  poverty_rate: 20.51
  homeownership_rate: 62.67
  unemployment_rate: 8.16
  median_home_value: 171200
  gini_index: 0.461
  vacancy_rate: 13.21
  race_white: 25586
  race_black: 2914
  race_asian: 729
  race_native: 670
  hispanic: 21886
  bachelors_plus: 9808
districts:
  - to: "us/states/nm/districts/03"
    rel: in-district
    area_weight: 0.9999
  - to: "us/states/nm/districts/senate/7"
    rel: in-district
    area_weight: 0.8643
  - to: "us/states/nm/districts/senate/27"
    rel: in-district
    area_weight: 0.1357
  - to: "us/states/nm/districts/house/67"
    rel: in-district
    area_weight: 0.5139
  - to: "us/states/nm/districts/house/63"
    rel: in-district
    area_weight: 0.3246
  - to: "us/states/nm/districts/house/64"
    rel: in-district
    area_weight: 0.1614
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, nm]
timestamp: "2026-07-03"
---

# Curry County, NM

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 47638 |
| Under 18 | 12637 |
| 18–64 | 28816 |
| 65+ | 6185 |
| Median household income | 57309 |
| Poverty rate | 20.51 |
| Homeownership rate | 62.67 |
| Unemployment rate | 8.16 |
| Median home value | 171200 |
| Gini index | 0.461 |
| Vacancy rate | 13.21 |
| White | 25586 |
| Black | 2914 |
| Asian | 729 |
| Native | 670 |
| Hispanic/Latino | 21886 |
| Bachelor's or higher | 9808 |

## Districts

- [NM-03](/us/states/nm/districts/03.md) — 100% (congressional)
- [NM Senate District 7](/us/states/nm/districts/senate/7.md) — 86% (state senate)
- [NM Senate District 27](/us/states/nm/districts/senate/27.md) — 14% (state senate)
- [NM House District 67](/us/states/nm/districts/house/67.md) — 51% (state house)
- [NM House District 63](/us/states/nm/districts/house/63.md) — 32% (state house)
- [NM House District 64](/us/states/nm/districts/house/64.md) — 16% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
