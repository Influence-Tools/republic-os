---
type: Jurisdiction
title: "San Juan County, NM"
classification: county
fips: "35045"
state: "NM"
demographics:
  population: 120942
  population_under_18: 30165
  population_18_64: 70316
  population_65_plus: 20461
  median_household_income: 55872
  poverty_rate: 23.08
  homeownership_rate: 71.2
  unemployment_rate: 7.26
  median_home_value: 193800
  gini_index: 0.4707
  vacancy_rate: 13.52
  race_white: 48274
  race_black: 759
  race_asian: 962
  race_native: 47935
  hispanic: 23976
  bachelors_plus: 20230
districts:
  - to: "us/states/nm/districts/03"
    rel: in-district
    area_weight: 0.9999
  - to: "us/states/nm/districts/senate/3"
    rel: in-district
    area_weight: 0.3678
  - to: "us/states/nm/districts/senate/22"
    rel: in-district
    area_weight: 0.2778
  - to: "us/states/nm/districts/senate/4"
    rel: in-district
    area_weight: 0.1686
  - to: "us/states/nm/districts/senate/2"
    rel: in-district
    area_weight: 0.1555
  - to: "us/states/nm/districts/senate/1"
    rel: in-district
    area_weight: 0.0302
  - to: "us/states/nm/districts/house/4"
    rel: in-district
    area_weight: 0.2766
  - to: "us/states/nm/districts/house/65"
    rel: in-district
    area_weight: 0.2214
  - to: "us/states/nm/districts/house/5"
    rel: in-district
    area_weight: 0.2213
  - to: "us/states/nm/districts/house/3"
    rel: in-district
    area_weight: 0.1428
  - to: "us/states/nm/districts/house/1"
    rel: in-district
    area_weight: 0.0644
  - to: "us/states/nm/districts/house/69"
    rel: in-district
    area_weight: 0.0565
  - to: "us/states/nm/districts/house/2"
    rel: in-district
    area_weight: 0.017
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, nm]
timestamp: "2026-07-03"
---

# San Juan County, NM

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 120942 |
| Under 18 | 30165 |
| 18–64 | 70316 |
| 65+ | 20461 |
| Median household income | 55872 |
| Poverty rate | 23.08 |
| Homeownership rate | 71.2 |
| Unemployment rate | 7.26 |
| Median home value | 193800 |
| Gini index | 0.4707 |
| Vacancy rate | 13.52 |
| White | 48274 |
| Black | 759 |
| Asian | 962 |
| Native | 47935 |
| Hispanic/Latino | 23976 |
| Bachelor's or higher | 20230 |

## Districts

- [NM-03](/us/states/nm/districts/03.md) — 100% (congressional)
- [NM Senate District 3](/us/states/nm/districts/senate/3.md) — 37% (state senate)
- [NM Senate District 22](/us/states/nm/districts/senate/22.md) — 28% (state senate)
- [NM Senate District 4](/us/states/nm/districts/senate/4.md) — 17% (state senate)
- [NM Senate District 2](/us/states/nm/districts/senate/2.md) — 16% (state senate)
- [NM Senate District 1](/us/states/nm/districts/senate/1.md) — 3% (state senate)
- [NM House District 4](/us/states/nm/districts/house/4.md) — 28% (state house)
- [NM House District 65](/us/states/nm/districts/house/65.md) — 22% (state house)
- [NM House District 5](/us/states/nm/districts/house/5.md) — 22% (state house)
- [NM House District 3](/us/states/nm/districts/house/3.md) — 14% (state house)
- [NM House District 1](/us/states/nm/districts/house/1.md) — 6% (state house)
- [NM House District 69](/us/states/nm/districts/house/69.md) — 6% (state house)
- [NM House District 2](/us/states/nm/districts/house/2.md) — 2% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
