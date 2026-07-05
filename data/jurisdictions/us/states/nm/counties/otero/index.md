---
type: Jurisdiction
title: "Otero County, NM"
classification: county
fips: "35035"
state: "NM"
demographics:
  population: 68816
  population_under_18: 15054
  population_18_64: 41685
  population_65_plus: 12077
  median_household_income: 55876
  poverty_rate: 19.26
  homeownership_rate: 66.99
  unemployment_rate: 8.56
  median_home_value: 162700
  gini_index: 0.4304
  vacancy_rate: 25.01
  race_white: 37156
  race_black: 2478
  race_asian: 1035
  race_native: 4327
  hispanic: 27267
  bachelors_plus: 13930
districts:
  - to: "us/states/nm/districts/02"
    rel: in-district
    area_weight: 0.9168
  - to: "us/states/nm/districts/01"
    rel: in-district
    area_weight: 0.0831
  - to: "us/states/nm/districts/senate/34"
    rel: in-district
    area_weight: 0.7894
  - to: "us/states/nm/districts/senate/33"
    rel: in-district
    area_weight: 0.2091
  - to: "us/states/nm/districts/house/54"
    rel: in-district
    area_weight: 0.7369
  - to: "us/states/nm/districts/house/56"
    rel: in-district
    area_weight: 0.2481
  - to: "us/states/nm/districts/house/51"
    rel: in-district
    area_weight: 0.0099
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, nm]
timestamp: "2026-07-03"
---

# Otero County, NM

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 68816 |
| Under 18 | 15054 |
| 18–64 | 41685 |
| 65+ | 12077 |
| Median household income | 55876 |
| Poverty rate | 19.26 |
| Homeownership rate | 66.99 |
| Unemployment rate | 8.56 |
| Median home value | 162700 |
| Gini index | 0.4304 |
| Vacancy rate | 25.01 |
| White | 37156 |
| Black | 2478 |
| Asian | 1035 |
| Native | 4327 |
| Hispanic/Latino | 27267 |
| Bachelor's or higher | 13930 |

## Districts

- [NM-02](/us/states/nm/districts/02.md) — 92% (congressional)
- [NM-01](/us/states/nm/districts/01.md) — 8% (congressional)
- [NM Senate District 34](/us/states/nm/districts/senate/34.md) — 79% (state senate)
- [NM Senate District 33](/us/states/nm/districts/senate/33.md) — 21% (state senate)
- [NM House District 54](/us/states/nm/districts/house/54.md) — 74% (state house)
- [NM House District 56](/us/states/nm/districts/house/56.md) — 25% (state house)
- [NM House District 51](/us/states/nm/districts/house/51.md) — 1% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
