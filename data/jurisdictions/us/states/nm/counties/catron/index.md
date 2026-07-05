---
type: Jurisdiction
title: "Catron County, NM"
classification: county
fips: "35003"
state: "NM"
demographics:
  population: 3743
  population_under_18: 230
  population_18_64: 1733
  population_65_plus: 1780
  median_household_income: 49864
  poverty_rate: 24.78
  homeownership_rate: 93.8
  unemployment_rate: 4.21
  median_home_value: 167000
  gini_index: 0.3875
  vacancy_rate: 47.52
  race_white: 2914
  race_black: 66
  race_asian: 12
  race_native: 142
  hispanic: 588
  bachelors_plus: 1430
districts:
  - to: "us/states/nm/districts/02"
    rel: in-district
    area_weight: 0.9999
  - to: "us/states/nm/districts/senate/35"
    rel: in-district
    area_weight: 0.9998
  - to: "us/states/nm/districts/house/49"
    rel: in-district
    area_weight: 0.8835
  - to: "us/states/nm/districts/house/39"
    rel: in-district
    area_weight: 0.1163
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, nm]
timestamp: "2026-07-03"
---

# Catron County, NM

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 3743 |
| Under 18 | 230 |
| 18–64 | 1733 |
| 65+ | 1780 |
| Median household income | 49864 |
| Poverty rate | 24.78 |
| Homeownership rate | 93.8 |
| Unemployment rate | 4.21 |
| Median home value | 167000 |
| Gini index | 0.3875 |
| Vacancy rate | 47.52 |
| White | 2914 |
| Black | 66 |
| Asian | 12 |
| Native | 142 |
| Hispanic/Latino | 588 |
| Bachelor's or higher | 1430 |

## Districts

- [NM-02](/us/states/nm/districts/02.md) — 100% (congressional)
- [NM Senate District 35](/us/states/nm/districts/senate/35.md) — 100% (state senate)
- [NM House District 49](/us/states/nm/districts/house/49.md) — 88% (state house)
- [NM House District 39](/us/states/nm/districts/house/39.md) — 12% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
